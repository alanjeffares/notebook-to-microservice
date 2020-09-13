import matplotlib.pyplot as plt
import seaborn as sns

from src.utils.data_utils import load_data


def main():
    data = load_data()
    sns.set_style('whitegrid')
    sns.pairplot(data, hue='species', height=3)
    plt.show()


if __name__ == 'main':
    main()
