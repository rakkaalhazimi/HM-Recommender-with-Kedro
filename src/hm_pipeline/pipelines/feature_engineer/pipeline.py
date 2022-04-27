"""
This is a boilerplate pipeline 'feature_engineer'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import time_transform


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=time_transform,
                inputs=["transactions_train_date"],
                outputs="transactions_train_time_ft"
            )
        ]
    )
