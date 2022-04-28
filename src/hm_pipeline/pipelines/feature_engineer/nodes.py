"""
This is a boilerplate pipeline 'feature_engineer'
generated using Kedro 0.18.0
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import FunctionTransformer


# Time Features
# ===============
def sin_transformer(period):
	return FunctionTransformer(lambda x: np.sin(x / period * 2 * np.pi))


def cos_transformer(period):
	return FunctionTransformer(lambda x: np.cos(x / period * 2 * np.pi))


def get_time_factor(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert datetime features into unique integer

    """
    # Factorize days
    day_factor, _ = pd.factorize(df["t_dat"])

    # Delete columns to save memory
    del df["t_dat"]

    # Add new columns
    df["day"] = day_factor
    df["week"] = (day_factor // 7)

    return df


def time_transform(df: pd.DataFrame):
    # Fetch time factors
    df = pd.DataFrame({"t_dat": df["t_dat"].unique()})
    df = get_time_factor(df)

    # Day index to sin and cos
    df["day_sin"] = sin_transformer(365).fit_transform(df["day"])
    df["day_cos"] = cos_transformer(365).fit_transform(df["day"])

    df["week_sin"] = sin_transformer(52).fit_transform(df["week"])
    df["week_cos"] = cos_transformer(52).fit_transform(df["week"])

    return df


def feature_engineer(transactions_train: pd.DataFrame):
    transactions_train_time_ft = time_transform(transactions_train)

    return transactions_train_time_ft


# Categorical Features
# ====================