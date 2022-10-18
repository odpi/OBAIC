from typing import Any, ABCMeta

from obaic.model import ObaicModel, ObaicOutput

class ObaicOutput:
    values: list[Any]

class ObaicResponse(metaclass=ABCMeta): pass

class ModelResponse(ObaicResponse): 
    models: list[ObaicModel]

class PredictionResponse(ObaicResponse): 
    prediction: list[ObaicOutput]