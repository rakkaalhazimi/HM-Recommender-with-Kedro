"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from kedro.extras.datasets import pandas; pandas.ParquetDataSet
from .pipelines import data_trimmer as dtrim
from .pipelines import feature_engineer as fte


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_trimmer_pipeline = dtrim.create_pipeline()
    feature_engineering_pipeline = fte.create_pipeline()

    return {
        "__default__": data_trimmer_pipeline,
        "dtrim": data_trimmer_pipeline,
        "fte": feature_engineering_pipeline
    }
