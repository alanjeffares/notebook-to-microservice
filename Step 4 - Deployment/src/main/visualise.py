import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import logging
from PIL import Image
from src.utils.data_utils import load_data
from src.utils.config import get_default

logger = logging.getLogger(__name__)

IMG_PATH = get_default('flask_app', 'img_path')


def main(*args):
    matplotlib.use('agg')
    data = load_data()
    logger.debug('Creating visualisation')
    sns.set_style('whitegrid')
    sns.pairplot(data, hue='species', height=3)
    logger.debug('Saving image')
    plt.savefig(IMG_PATH)
    if 'flask_app' not in args:
        logger.info('Visualising image locally')
        logger.debug('This should not be done in Flask')
        image = Image.open(IMG_PATH)
        image.show()


if __name__ == 'main':
    main()
