from abc import ABCMeta, abstractmethod

from obaic.sourcedefinitions import MLSourceDefinition

from .model import ObaicModel, ObaicModelInput, ObaicModelOutput
from typing import Iterable

class MLSource(metaclass=ABCMeta):
    # A single positional parameter is passed to construct the Source
    def __init__(self, __x: MLSourceDefinition) -> None: pass

    @abstractmethod
    def connect(self) -> None: pass

    @abstractmethod
    def list_models(self) -> Iterable[ObaicModel]: pass

    @abstractmethod
    def predict(self, model: ObaicModel, input: ObaicModelInput) -> ObaicModelOutput: pass