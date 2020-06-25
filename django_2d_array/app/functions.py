import    string
alphabet  = list(string.ascii_uppercase)

def grid_top_row(columns):
    row        = []
    cells      = []
    for i in range(0, columns):
        cells.append( "A" + str(i) )
    row.append(cells)
    return row

def grid_top_left_cells(i, columns_copy, rows_copy):
    cell_number          = (columns_copy * 2) + ( (rows_copy - 2) * 2)
    top_left_number      = ((i - 1) * 7) 
    cells                = []
    for j in range(0, i):
        cells.append(alphabet[j]  + str(cell_number + top_left_number - 1) )
        top_left_number  -= 7
    return cells

def grid_top_middle_cells(i, columns):
    reduce_cells_until = columns - i
    number             = 0
    cells              = []
    for _ in range(i, reduce_cells_until):
        cells.append( alphabet[i] + str(number) )
        number += 1
    return cells

def grid_top_right_cells(i, columns):
    top_right_number  = (columns + i - 1) - ((i - 1) * 3) 
    cells             = []
    for j in range(i, 0, -1):
        cells.append( alphabet[j - 1] + str(top_right_number)  )
        top_right_number += 3
    return cells

def grid_bottom_left_cells(j, columns_copy, rows_copy, increment_1):
    bottom_left_number = (columns_copy * 2) + ((rows_copy - 2) * 2) + ((j - 1) * 7)
    cells              = []
    for k in range(0, j - 1):
        cells.append(  str(alphabet[k])  + str(bottom_left_number - (increment_1 * 2)  - 1) )
        bottom_left_number -= 7
    return cells

def grid_bottom_middle_cells(j, columns_copy, rows_copy, columns, increment_1):
    max_left_side_number  = (columns_copy * 2) + ((rows_copy - 2) * 2) - ((increment_1 * 2) + 1)
    increase_cells_until  = columns - (j* 2) + 2
    cells = []
    for _ in range(0,  increase_cells_until):
        cells.append( alphabet[ j  - 1] + str( max_left_side_number) )
        max_left_side_number -= 1
    return cells

def grid_bottom_right_cells(j, columns, increment_1):
    max_left_side         = columns + j - ((j - 1) * 3) + (increment_1 * 2) + 2
    cells = []
    for k in range(j - 1, 0, -1):
        cells.append( str(alphabet[k - 1]) + str(max_left_side) )
        max_left_side += 3
    return cells

def grid_bottom_row(columns, rows):
    j        = (columns * 2) + rows - 3
    cells    = []
    for _ in range(0, columns):
        cells.append("A" + str(j) )
        j -= 1
    return cells