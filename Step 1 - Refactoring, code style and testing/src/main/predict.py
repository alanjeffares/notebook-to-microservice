import numpy as np
import sys
from src.utils.model_utils import load_model
from src.utils.data_utils import parse_observation


def main():
    gscv = load_model()

    new_obs = parse_observation([5.1, 3.8, 1.5, 0.3])

    prediction = gscv.predict(new_obs)
    print('predicted class:', prediction[0])


if __name__ == 'main':
    main()
