"""
This is a boilerplate pipeline 'retrieval_model'
generated using Kedro 0.18.0
"""
import pandas as pd


def get_id_vocabulary(transactions_train: pd.DataFrame):
    customer_id = transactions_train["customer_id"]
    article_id = transactions_train["article_id"]

    unique_customer_id = customer_id.unique().astype(str)
    unique_article_id = article_id.unique().astype(str)
    
    article_vocabulary = "\n".join(unique_article_id)
    customer_vocabulary = "\n".join(unique_customer_id)

    return article_vocabulary, customer_vocabulary