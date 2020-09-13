import unittest
import sys
import pandas as pd
sys.path.append('../..')
sys.path.append('.')
import src.utils.data_utils as data_utils  # noqa: E402

MOCK_DF = pd.DataFrame(
    {'X': [1, 2, 3, 4, 5, 6, 7, 8],
     'Y': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']})

MOCK_LIST = [1, 2, 3]


class DataUtilsUnitTest(unittest.TestCase):
    def test_stratified_split(self):
        train_df, test_df = data_utils.stratified_split(MOCK_DF, 'Y', 1)
        self.assertEqual(train_df.shape[0], 6,
                         '6 observations in training set')
        self.assertEqual(test_df.shape[0], 2,
                         '2 observations in testing set')
        A_count = train_df[train_df['Y'] == 'A'].shape[0]
        B_count = train_df[train_df['Y'] == 'B'].shape[0]
        self.assertEqual(A_count, B_count,
                         'Same number of each class in training set')

    def test_parse_observation(self):
        arr = data_utils.parse_observation(MOCK_LIST)
        self.assertEqual(arr.shape, (1, 3),
                         'Dimensions should be 1 x 3')
        self.assertEqual(arr[0, 0], 1,
                         'Element (0,1) should be 1')


if __name__ == "__main__":
    unittest.main()
