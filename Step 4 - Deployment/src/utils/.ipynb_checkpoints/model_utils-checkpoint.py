from sklearn.base import BaseEstimator
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import GridSearchCV
import pickle
import logging

logger = logging.getLogger(__name__)


class ClfSwitcher(BaseEstimator):
    """A Custom BaseEstimator that can switch between classifiers"""
    def __init__(self, estimator=None):
        self.estimator = estimator

    def set_params(self, **parameters):
        for parameter, value in parameters.items():
            setattr(self, parameter, value)
        return self

    def fit(self, X, y=None, **kwargs):
        self.estimator.fit(X, y)
        return self

    def predict(self, X, y=None):
        return self.estimator.predict(X)


def format_params(estimator: BaseEstimator, **kwargs) -> dict:
    """Format parameters for GridSearchCV.

    Args:
        estimator (BaseEstimator): Estimator to be formated.
        kwargs: Parameters corresponding to the estimator being
            passed.

    Returns:
        dict: Formatted estimator with keyword arguments.

    """
    params = {'clf__estimator': [estimator]}
    for key, value in kwargs.items():
        params['clf__estimator__' + key] = value
    return params


def save_model(model: GridSearchCV) -> None:
    """Save latest trained model to models folder."""
    logger.info('Saving model')
    path = 'src/resources/models/'
    filename = 'latest_model.pkl'
    pickle.dump(model, open(path + filename, 'wb'))


def load_model() -> GridSearchCV:
    """Load latest trained model from models folder."""
    logger.info('Loading model')
    path = 'src/resources/models/'
    filename = 'latest_model.pkl'
    model = pickle.load(open(path + filename, 'rb'))
    return model
