import numpy as np
from sklearn.metrics import mean_squared_error

def train_test_split_by_date(df, date_col, cutoff):
    """
    Split dataframe into train/test based on date cutoff.

    Parameters
    ----------
    df : pandas.DataFrame
    date_col : str
        Column name containing datetime values
    cutoff : str
        Date string used as split point

    Returns
    -------
    train_df, test_df : pandas.DataFrame
    """
    train = df[df[date_col] <= cutoff].copy()
    test = df[df[date_col] > cutoff].copy()
    return train, test


def rmse(y_true, y_pred):
    """
    Compute root mean squared error.

    Parameters
    ----------
    y_true : array-like
    y_pred : array-like

    Returns
    -------
    float
    """
    return mean_squared_error(y_true, y_pred) ** 0.5
