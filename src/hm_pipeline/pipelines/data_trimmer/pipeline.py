"""
This is a boilerplate pipeline 'data_trimmer'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import trim_data_memory


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=trim_data_memory,
                inputs=["articles_raw", "customers_raw", "transactions_train_raw"],
                outputs=["articles", "customers", "transactions_train"]
            ),
        ]
    )
