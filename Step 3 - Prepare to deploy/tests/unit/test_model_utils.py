import unittest
import sys
import warnings
from sklearn.model_selection import GridSearchCV
sys.path.append('../..')
sys.path.append('.')
import src.utils.model_utils as model_utils  # noqa: E402

MOCK_PARAM_DICT = {'clf__estimator': ['mock_estimator'],
                   'clf__estimator__arg1': 1,
                   'clf__estimator__arg2': 'string'}


def ignore_warnings(test_func):
    """Decorator to ignore warnings in unittest"""
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)
    return do_test


class ModelUtilsUnitTest(unittest.TestCase):
    def test_format_params(self):
        parameters = model_utils.format_params(estimator='mock_estimator',
                                               arg1=1,
                                               arg2='string')
        self.assertEqual(parameters, MOCK_PARAM_DICT)

    @ignore_warnings
    def test_save_load_model(self):
        model_utils.save_model(GridSearchCV)
        loaded_model = model_utils.load_model()
        self.assertEqual(GridSearchCV, loaded_model)


if __name__ == "__main__":
    unittest.main()
