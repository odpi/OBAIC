from abc import ABCMeta, abstractmethod
from obaic.requests import PredictionRequest

from obaic.sourcedefinitions import MLSourceDefinition

from obaic.model import ObaicModel, ModelRequest
from typing import Iterable

class MLSource(metaclass=ABCMeta):
    # A single positional parameter is passed to construct the MLSource
    def __init__(self, __x: MLSourceDefinition) -> None: pass

    @abstractmethod
    def list_models(self, model_request: ModelRequest) -> Iterable[ObaicModel]: pass

    @abstractmethod
    async def list_models_async(self, model_request: ModelRequest) -> Iterable[ObaicModel]: pass

    @abstractmethod
    def predict(self, model: ObaicModel, prediction_request: PredictionRequest) -> PredictionResponse: pass

    @abstractmethod
    async def predict_async(self, model: ObaicModel, prediction_request: PredictionRequest) -> PredictionResponse: pass

    @abstractmethod
    async def train(self): pass

    @abstractmethod
    async def train_async(self): pass
