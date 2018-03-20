from unittest import TestCase
from ..build import q01_create_dict
from inspect import getfullargspec
import pandas as pd

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])
names_dict = q01_create_dict(data)


class TestLinearRegression(TestCase):
    def test_arguments(self):

        # Input parameters tests
        args = getfullargspec(q01_create_dict)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))

    def test_defaults(self):
        args = getfullargspec(q01_create_dict)
        self.assertEqual(args[3], (None), "Expected default values do not match given default values")

    # Return type tests
    def test_return(self):
        self.assertIsInstance(names_dict,dict,
                              "Expected data type for return value is `dictionary`, you are returning %s" % (
                                  type(names_dict)))