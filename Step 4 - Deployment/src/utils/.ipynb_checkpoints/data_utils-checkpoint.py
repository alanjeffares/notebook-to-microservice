import pandas as pd
import numpy as np
import logging
from typing import Tuple

logger = logging.getLogger(__name__)


def load_data() -> pd.DataFrame:
    """Loads Iris data from online csv file"""
    logger.info('Loading data')
    file = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'  # noqa: E402
    df = pd.read_csv(file)
    return df


def stratified_split(data: pd.DataFrame,
                     target: str,
                     n_samples: int) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Stratified data split.

    Splits data into training and testing dataframes whilst stratifying
    to maintain target variable proportions.

    Args:
        data (DataFrame): Full dataframe including predictors as well as
            target variable.
        target (str): The name of the column containing the target
            variable.
        n_samples (int): The number of samples to include in the test
            set from each target label category.

        Returns:
            tuple: The training and testing dataframes.

    """
    logger.info('Splitting train and test sets')
    n = min(n_samples, data[target].value_counts().min())
    test_df = data.groupby(target).apply(lambda x: x.sample(n))
    test_df.index = test_df.index.droplevel(0)
    train_df = data[~data.index.isin(test_df.index)]
    return train_df, test_df


def parse_observation(obs: list) -> np.array:
    """Reshape a list into a 1 x len(obs) numpy array"""
    new_obs = np.array(obs).reshape(1, -1)
    return new_obs
