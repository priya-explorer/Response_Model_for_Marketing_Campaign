import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

# TODO: Binary Classification Metric
def bin_class_metrics(model_name, y_test, y_pred, y_score, metric_output=True, plot_auc_roc=True):
    """A binary classification metrics, plot AUC ROC and Precision-Recall curves.

    Args:
        model_name (str): The model name identifier
        y_test (series): Contains the test label values
        y_pred (series): Contains the predicted values
        y_score (series): Contains the predicted scores
        metric_output (bool): Print the classification metrics and thresholds values
        plot_auc_roc (bool): Plot AUC ROC, Precision-Recall, and Threshold curves

    Returns:
        dataframe: The combined metrics in single dataframe"""

    # TODO: Create Performance Metrics
    binary_class_metrics = {
        'Accuracy': metrics.accuracy_score(y_test, y_pred),
        'Precision': metrics.precision_score(y_test, y_pred),
        'Recall': metrics.recall_score(y_test, y_pred),
        'F1 Score': metrics.f1_score(y_test, y_pred),
        'ROC AUC': metrics.roc_auc_score(y_test, y_score)
    }

    # TODO: Create a dataframe of binary classification metric scores
    df_metrics = pd.DataFrame.from_dict(binary_class_metrics, orient='index')
    df_metrics.columns = [model_name]

    # AUC Metric
    fpr, tpr, thresh_roc = metrics.roc_curve(y_test, y_score)
    roc_auc = metrics.auc(fpr,tpr)

    # TODO: To print Confusion Matrix, Classification Report
    if metric_output:
        print('---------------------------------------------------------------------')
        print(model_name.center(80,' '))
        print('---------------------------------------------------------------------')
        print('\nConfusion Matrix:')
        print(metrics.confusion_matrix(y_test, y_pred))
        print('\nClassification Report:')
        print(metrics.classification_report(y_test, y_pred))

    # TODO: Plot AUC
    if plot_auc_roc:
        plt.figure(1)
        lw = 2
        plt.plot(fpr, tpr, color='green',
                 lw=lw, label='AUC = %0.2f' % roc_auc)
        plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')

        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('{} - Area Under Curve'.format(model_name))
        plt.legend(loc="lower right")
        plt.show()

    return df_metrics

# TODO: Train, Test Score for Classifier Model
def train_test_score(clf, x_train, y_train, x_test, y_test):
    score_dict = {
        "Training Score: ": clf.score(x_train, y_train),
        "Testing Score: ": clf.score(x_test, y_test)
          }

    for key, value in score_dict.items():
        print(key, value)