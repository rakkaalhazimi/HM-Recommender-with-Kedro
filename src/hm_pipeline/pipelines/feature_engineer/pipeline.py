"""
This is a boilerplate pipeline 'feature_engineer'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import feature_engineer


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=feature_engineer,
                inputs=["transactions_train"],
                outputs="transactions_train_time_ft"
            )
        ]
    )
