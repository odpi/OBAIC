from abc import ABCMeta, abstractmethod
from obaic.requests import PredictionRequest

from obaic.sourcedefinitions import MLSourceDefinition

from obaic.model import ObaicModel, ObaicScore
from typing import Iterable

class MLSource(metaclass=ABCMeta):
    # A single positional parameter is passed to construct the MLSource
    def __init__(self, __x: MLSourceDefinition) -> None: pass

    @abstractmethod
    def connect(self) -> None: pass

    @abstractmethod
    def close(self) -> None: pass

    @abstractmethod
    async def list_models(self) -> Iterable[ObaicModel]: pass

    @abstractmethod
    async def predict(self, model: ObaicModel, prediction_request: PredictionRequest) -> PredictionResponse: pass

    @abstractmethod
    async def train(self): pass
