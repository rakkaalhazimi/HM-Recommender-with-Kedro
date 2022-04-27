"""
This is a boilerplate pipeline 'feature_engineer'
generated using Kedro 0.18.0
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import FunctionTransformer


def sin_transformer(period):
	return FunctionTransformer(lambda x: np.sin(x / period * 2 * np.pi))


def cos_transformer(period):
	return FunctionTransformer(lambda x: np.cos(x / period * 2 * np.pi))


def get_time_factor(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert datetime features into unique integer

    """
    # Convert date string to datetime
    df["t_dat"] = pd.to_datetime(df["t_dat"])

    # Factorize days
    day_factor, _ = pd.factorize(df["t_dat"])

    # Delete columns to save memory
    del df["t_dat"]

    # Add new columns
    df["day"] = day_factor + 1
    df["week"] = (day_factor // 7) + 1

    return df


def time_transform(transactions_train_date: pd.DataFrame):
    # Fetch time factors
    transactions_train_time_ft = get_time_factor(transactions_train_date)

    # Day index to sin and cos
    transactions_train_time_ft["day_sin"] = sin_transformer(365).fit_transform(transactions_train_time_ft["day"])
    transactions_train_time_ft["day_cos"] = cos_transformer(365).fit_transform(transactions_train_time_ft["day"])

    return transactions_train_date
