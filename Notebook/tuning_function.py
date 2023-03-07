# Importing necessary files
import pandas as pd
import numpy as np
import time
from sklearn.model_selection import GridSearchCV

# TODO: GridSearchCV Function
def grid_search(model_name, clf, x_train, y_train, cv_value=5, param_dict=None, s=None):

    """Grid Search hyper parameter tuning on a classifier.

        Args:
            model_name (str): The model name identifier
            clf (classifier object): The classifier to be tuned
            x_train (dataframe): Training dataframe with independent features X
            y_train (dataframe): Training dataframe with target features y
            cv_value (int) : Cross validation default value is 5
            param_dict (dict): Grid Search parameters
            s (int): The seed value needed to generate a random number

        Returns:
            Tuned Parameters for the classifier object"""

    np.random.seed(s)
    start = time.time()

    cv_model_grid = GridSearchCV(estimator=clf, param_grid = param_dict, n_jobs=-1, cv=cv_value)
    cv_model_grid.fit(x_train, y_train)

    end = time.time()

    print("---------------------------------------------------------------------")
    print(model_name.center(80,' '))
    print("---------------------------------------------------------------------")
    print("The time taken in grid search: {0: .2f}".format(end - start))
    return 'Best Parameters using grid search:', cv_model_grid.best_params_




