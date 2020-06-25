import json
import copy
import sys
import string
import time

from django.shortcuts              import render
from django.http                   import HttpResponse, Http404
from django.views.decorators.cache import never_cache
from app.models                    import Visit
from app.constants                 import BG_COLORS
from app.functions                 import *

def index(request):
    return render(request, 'index.html')

@never_cache
def grid_init(request):
    jsonn          = {}
    ip_address             = request.META.get('REMOTE_ADDR')

    try:
        visit              = Visit.objects.get(ip_address = ip_address)
    except:
        visit              = Visit.objects.create(
                                    ip_address = ip_address,
                                    grid       = json.dumps(grid_generator(4, 4)),
                                    cols       = 4,
                                    rows       = 4,
                                    rotation   = 0
                               )

    jsonn["data"] = {
                                'grid': json.loads(visit.grid),
                                'cols': visit.cols,
                                'rows': visit.rows,
                            }
    return HttpResponse(json.dumps(jsonn),  content_type='application/json')

def grid_generator(columns, rows):
    
    if not columns or not rows:
        return []

    elif columns == rows == 1:
        return [['A0']]

    if not rows % 2 == 0:
        return ['not odd rows']
    
    rows_half            = int(rows / 2)
 
    alphabet             = list(string.ascii_uppercase)

    columns_copy         = columns
    rows_copy            = rows

    jsonn                = []
    grid_size            = (columns * 2) + ((rows - 2) * 2)
    jsonn               += grid_top_row(columns)

    #first half of the grid
    for i in range(1 , rows_half):
        row                   = []
        row                  += grid_top_left_cells(i, columns_copy, rows_copy)
        row                  += grid_top_middle_cells(i, columns)
        row                  += grid_top_right_cells(i, columns)
        jsonn.append(row)

        columns_copy        -= 2
        rows_copy           -= 2

    #second half of the grid
    increment_1               = 0
    for j in range(rows_half, 1, -1):
        row                   = []
        row                  += grid_bottom_left_cells(j, columns_copy, rows_copy, increment_1)
        row                  += grid_bottom_middle_cells(j, columns_copy, rows_copy, columns, increment_1)
        row                  += grid_bottom_right_cells(j, columns, increment_1)

        increment_1          += 1
        columns_copy         += 2
        rows_copy            += 2
        jsonn.append(row) 

    row         = grid_bottom_row(columns, rows)
    jsonn.append(row)
    return jsonn

def grid_rotate(request, rotations):

    if not rotations:
        raise Http404("No rotations")

    rotations            = int(rotations)
    ip_address           = request.META.get('REMOTE_ADDR')
    try:
        visit            = Visit.objects.get(ip_address = ip_address)
        grid             = json.loads(visit.grid)
    except:
        grid_init(request)
        raise Http404()
    
    rows               = len(grid)
    cols               = len(grid[0])
    
    tables             = {}
    number_of_frames   = int(round(len(grid) / 2))

    if rows > cols:
        number_of_frames  = int(round(len(grid[0]) / 2))

    for i_frame in range(0, number_of_frames): 
        tables[i_frame]           = [ (i_frame, i_frame)]
        row_down            = (rows - 1)  - i_frame
        right_side          = (cols - 1)  - i_frame
        if i_frame == row_down:
            #only top row
            for i in range(i_frame, (cols - i_frame) - 1):
                tables[i_frame].append((i_frame, i + 1))
        else:
            #top row of table
            for i in range(i_frame, (cols - i_frame) - 1):
                tables[i_frame].append((i_frame, i + 1))
            #right side of table
            for i in range(i_frame + 1, (rows - i_frame) - 1 ):
                tables[i_frame].append((i, right_side))
            #bottom row of table
            for i in range((cols - i_frame) - 1 , i_frame, -1):
                tables[i_frame].append((row_down, i))
            #left side of table
            for i in range(row_down, i_frame, -1):
                tables[i_frame].append((i, i_frame))

    tables_copy     = copy.deepcopy(tables)
    initial         = 0
    for i_frame in range(0, number_of_frames): 

        normal_returns_at        = len(tables[i_frame])
        if rotations >= normal_returns_at:
            initial                         = int(int(rotations / normal_returns_at) * normal_returns_at)
    
        for _ in range(initial, rotations):
            temp               = {}
            temp[i_frame]      = tables_copy[i_frame][1:]
            zero               = tables_copy[i_frame][0]
            temp[i_frame].append( zero)
            tables_copy[i_frame] = temp[i_frame]


    grid_copy = copy.deepcopy(grid)
    for k in range(0, number_of_frames): 
        for coord in range(0, len(tables[k]) ):
            grid_copy[ tables[k][coord][0] ][  tables[k][coord][1] ] = grid[ tables_copy[k][coord][0] ][  tables_copy[k][coord][1] ] 

    visit.grid      = json.dumps(grid_copy)
    visit.save()

    jsonn            = {}
    jsonn["data"]    = { 
                        'grid':  grid_copy,
                        'cols':  cols
                         }

    return HttpResponse(json.dumps(jsonn),  content_type='application/json')