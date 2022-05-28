"""
This is a boilerplate pipeline 'retrieval_model'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import get_id_vocabulary


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=get_id_vocabulary,
                inputs=["transactions_train"],
                outputs=["article_vocabulary", "customer_vocabulary"]
            )
        ]
    )
