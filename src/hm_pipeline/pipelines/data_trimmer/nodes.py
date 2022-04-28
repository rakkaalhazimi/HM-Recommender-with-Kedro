"""
This is a boilerplate pipeline 'data_trimmer'
generated using Kedro 0.18.0
"""
from typing import List
import pandas as pd


def _long_id_to_int(long_id: str) -> int:
    """
    Convert customer id into memory safe integer

    """
    return int(long_id[-16:], base=16)


def trim_long_id(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Apply memory safe transformations onto specified column

    """
    df[columns] = df[columns].applymap(_long_id_to_int)
    return df


def trim_article_id(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply memory safe transformations onto article_id column

    """
    df["article_id"] = df["article_id"].astype("int32")
    return df



def trim_data_memory(articles_raw, customers_raw, transactions_train_raw):
    """
    Reduce dataframe memory usage by transforming specific columns

    """
    # Trim data
    articles = trim_article_id(articles_raw)
    customers = trim_long_id(customers_raw, columns=["customer_id", "postal_code"])
    transactions_train = trim_long_id(transactions_train_raw, columns=["customer_id"])
    transactions_train = trim_article_id(transactions_train)

    return articles, customers, transactions_train
