import numpy as np
import sys
import logging
from src.utils.model_utils import load_model
from src.utils.data_utils import parse_observation
from src.utils.config import get_default

logger = logging.getLogger(__name__)

VALUE = get_default('predict', 'value')


def main(**kwargs):
    gscv = load_model()

    if 'value' in kwargs:
        VALUE = kwargs.get('value')

    new_obs = parse_observation(VALUE)

    prediction = gscv.predict(new_obs)
    logger.info('Predicted class: {}'.format(prediction[0]))
    return prediction[0]


if __name__ == 'main':
    main()
