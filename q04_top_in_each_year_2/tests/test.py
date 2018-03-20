import sys, os
import pandas as pd
import numpy
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q04_top_in_each_year_2
from inspect import getfullargspec

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])
names_dict = q04_top_in_each_year_2(data)
array = [13.130481688989887,12.855623833780658,12.435705211584855,12.274968238419172,12.030442649038966,11.581008625697651]

class TestLinearRegression(TestCase):
    def test__arguments(self):

        # Input parameters tests
        args = getfullargspec(q04_top_in_each_year_2)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))

    def test__defaults(self):
        args = getfullargspec(q04_top_in_each_year_2)
        self.assertEqual(args[3], (None), "Expected default values do not match given default values")

    # Return type tests
    def test_return(self):
        self.assertIsInstance(names_dict,numpy.ndarray,
                              "Expected data type for return value is `dictionary`, you are returning %s" % (
                                  type(names_dict)))
    def test_return_1(self):
        self.assertEqual(list(names_dict), list(array),
                              "Expected data type for return value is `array`, you are returning %s" % (
                                  (names_dict)))