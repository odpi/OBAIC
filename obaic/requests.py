from obaic.credential import DataSourceCredential, MLSourceCredential
from typing import Any

from .sourcedefinitions import DataSourceDefinition
from typing import Optional, ABCMeta

class ObaicRequest(metaclass=ABCMeta):
    ml_src_credential: MLSourceCredential
    data_src_credential: DataSourceCredential

class ModelRequest(ObaicRequest):
    model_query: Optional[str]

class PredictionRequest(ObaicRequest):
    data_src: Optional[DataSourceDefinition]
    data_query: Optional[str]
    data: Optional[list[any: Any]]