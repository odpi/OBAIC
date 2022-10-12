from obaic.credentials import DataSourceCredential, MLSourceCredential
from obaic.sourcedefinitions import DataSourceDefinition

from typing import Optional, ABCMeta

class ObaicRequest(metaclass=ABCMeta):
    ml_src_credential: MLSourceCredential
    data_src_credential: Optional[DataSourceCredential]

class ModelRequest(ObaicRequest):
    model_query: Optional[str]

class PredictionRequest(ObaicRequest):
    data_src: Optional[DataSourceDefinition]
    data_query: Optional[str]
    data: Optional[list[any: dict]]