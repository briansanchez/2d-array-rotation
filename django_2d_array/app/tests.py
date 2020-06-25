import pytest
from django.test import TestCase
from app.views import grid_generator

class TestGridGenerator(TestCase):

    def test_0_x_0(self):
        columns, rows  = 0, 0
        response = grid_generator(columns, rows)
        self.assertEqual(response, [] )

    def test_0_x_1(self):
        columns, rows  = 0, 1
        response = grid_generator(columns, rows)
        self.assertEqual(response, [] )

    def test_1_x_0(self):
        columns, rows  = 1, 0
        response = grid_generator(columns, rows)
        self.assertEqual(response, [] )

    def test_2_x_2(self):
        columns, rows = 2, 2
        response      = grid_generator(columns, rows)
        self.assertEqual(response, [['A0', 'A1'], ['A3', 'A2']])

    def test_2_x_3(self):
        columns, rows  = 2, 3
        response       = grid_generator(columns, rows)
        self.assertEqual(response, ['not odd rows'])

    def test_2_x_4(self):
        columns, rows  = 2, 4
        response       = grid_generator(columns, rows)
        self.assertEqual(response, [['A0', 'A1'], ['A7', 'A2'], ['A6', 'A3'], ['A5', 'A4']])

    def test_odd_columns_odd_rows_3_3(self):
        columns, rows = 3, 3
        response      = grid_generator(columns, rows)
        self.assertEqual(response, ['not odd rows'])

    def test_3_x_2(self):
        columns, rows = 3, 2
        response      = grid_generator(columns, rows)
        self.assertEqual(response, [['A0', 'A1', 'A2'], ['A5', 'A4', 'A3']] )

    def test_1_x_2(self):
        columns, rows  = 1, 2
        response = grid_generator(columns, rows)
        self.assertEqual(response, [['A0'], ['A1']] )

    def test_10_x_2(self):
        columns, rows  = 10, 2
        response = grid_generator(columns, rows)
        self.assertEqual(response, [['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'], ['A19', 'A18', 'A17', 'A16', 'A15', 'A14', 'A13', 'A12', 'A11', 'A10']] )

    def test_1_x_1(self):
        columns, rows  = 1, 1
        response = grid_generator(columns, rows)
        self.assertEqual(response, [['A0']] )

    @pytest.mark.skip(reason = "fixing test_6_x_6")
    def test_4_x_4(self):
        columns, rows = 4, 4
        response      = grid_generator(columns, rows)
        self.assertEqual(response, [['A0', 'A1', 'A2', 'A3'], 
                                    ['A11', 'B0', 'B1', 'A4'],
                                    ['A10', 'B3', 'B2', 'A5'],
                                    ['A9', 'A8', 'A7', 'A6'],
                                    ])

    def test_6_x_6(self):
        columns, rows = 6, 6
        response      = grid_generator(columns, rows)
        self.assertEqual(response, [
                                    ['A0',  'A1', 'A2', 'A3', 'A4', 'A5'],
                                    ['A19', 'B0', 'B1', 'B2', 'B3', 'A6'],
                                    ['A18', 'B11', 'C0', 'C1', 'B4', 'A7'],
                                    ['A17', 'B10', 'C3', 'C2', 'B5', 'A8'],
                                    ['A16', 'B9', 'B8', 'B7', 'B6', 'A9'],
                                    ['A15', 'A14', 'A13', 'A12', 'A11', 'A10'],
                                    
                                    ])

