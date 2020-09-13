from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from src.utils.data_utils import load_data, stratified_split
from src.utils.model_utils import ClfSwitcher, format_params, save_model


def main():
    data_df = load_data()
    train_df, test_df = stratified_split(
        data=data_df, target='species', n_samples=5)

    # compile the modelling pipeline for CV using sklearn
    steps = [('scaler', StandardScaler()), ('clf', ClfSwitcher())]
    pipeline = Pipeline(steps)
    parameters = [format_params(LogisticRegression(),
                                C=[0.5, 0.75, 1]),
                  format_params(DecisionTreeClassifier(),
                                max_depth=[2, 3, None],
                                min_samples_leaf=[1, 2]),
                  format_params(LinearDiscriminantAnalysis())]

    gscv = GridSearchCV(pipeline, parameters, cv=3, scoring='accuracy')

    print('training model')
    gscv.fit(train_df.iloc[:, :4], train_df['species'])

    # print results
    print('best model: \n\n', gscv.best_estimator_)
    print('\ntest set accuracy: ', gscv.score(
        test_df.iloc[:, :4], test_df['species']))

    save_model(gscv)


if __name__ == 'main':
    main()
