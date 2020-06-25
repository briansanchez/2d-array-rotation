
# 2d Array Rotation
  Python generates & rotates counter clockwise the grid, angular shows the magic!.
  The initial grid size is 4 columns by 4 rows.
  

[![2d Array Rotation](https://2d-array-rotation.com/static/images/matrix_rotation.jpg)](https://2d-array-rotation.com/)


#### Requirements
- Python 3.7 & up
- Virtual Environment (pipenv)
- Angular 4 & up

### Initial Setup
```
$ git clone git@github.com:briansanchez/2d-array-rotation.git
$ cd 2d-array-rotation

# activate pipenv
$ pipenv shell
```

### Django
```
$ cd django_2d_array
$ install -r requirements.txt
```

Then we will modify `django_2d_array/my_secrets.py`:

```python
#get your own SECRET_KEY from https://djecrety.ir/
SECRET_KEY = '***'  
```
finally

```
$ python manage.py migrate
$ python manage.py runserver
```

### Angular

open a new terminal and run angular

```
cd angular_2d_array
npm install
ng serve
```

## Algorithm Explanation

#### Grid Creation
My approach is to divide the grid in 8 sections, each section will generate cells independently.

1. Top row
2. Top left side of the grid
3. Top middle section of the grid
4. Top right side of the grid
5. Bottom left side of the grid
6. Bottom middle section of the grid
7. Bottom right side of the grid
8. Bottom row

#### Grid Rotation
Let's use imaginary iframes.

1. Iterate the rows and cols of the grid, having # of iframes = size of the grid / 2.
1. Save the position of the coords for each iframe in an array.
2. Make a copy of each iframe and rotate the copy.
3. Potential problem could be having 1 million of rotations, so let's optimize this by using this formula to have the initial number to start the rotation: (n rotations / total_cells_in_frame) * total_cells_in_frame, meaning where the grid comes back to original position "for each iframe".
4. After n Rotations, display the grid using step 1 with coords rotated in step 2.


## Python exercises in TDD style

### How to run tests locally in Linux
Locally running the unit testing requires [pytest](http://pytest.org)

Then you can run the tests with:
```
$ pytest django_2d_array/app/tests.py
```

You can run a single test case like this:
```
$ pytest django_2d_array/app/tests.py -k 'test_6_x_6'
```

You can run multiple test cases with:
```
$ pytest django_2d_array/app/tests.py -k 'test_6_x_6 or test_10_x_2 or test_2_x_4'
```
 
