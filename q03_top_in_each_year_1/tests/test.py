import sys, os
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q03_top_in_each_year_1
from inspect import getfullargspec

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])
names_dict = q03_top_in_each_year_1(data)


class TestLinearRegression(TestCase):
    def test__arguments(self):

        # Input parameters tests
        args = getfullargspec(q03_top_in_each_year_1)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))

    def test__defaults(self):
        args = getfullargspec(q03_top_in_each_year_1)
        self.assertEqual(args[3], (None), "Expected default values do not match given default values")

    # Return type tests
    def test_return(self):
        self.assertIsInstance(names_dict,dict,
                              "Expected data type for return value is `dictionary`, you are returning %s" % (
                                  type(names_dict)))