from abc import ABCMeta, abstractmethod

from obaic.model import ObaicModel, ObaicOutput
from typing import Any, Dict, Iterable, List, Sequence

ObaicValue = Any
ObaicFeature = Sequence[Any]
ObaicOutput = Sequence[Any]

class MLSource(metaclass=ABCMeta):

    def __init__(self, ml_src_parameters: Dict[str, str], ml_src_credentials: Dict[str, str]) -> None: pass

    @abstractmethod
    def list_models(self, model_query: str) -> Iterable[ObaicModel]: pass

    @abstractmethod
    async def list_models_async(self, model_query: str) -> Iterable[ObaicModel]: pass

    @abstractmethod
    def predict_with_features(self, model: ObaicModel, features: List[ObaicFeature] ) -> Iterable[ObaicOutput]: pass

    @abstractmethod
    async def predict_with_data_ref_async(self, model: ObaicModel, 
                                                data_src_parameters: Dict[str, str],
                                                data_src_credentials: Dict[str, str], 
                                                data_query: str) -> Iterable[ObaicOutput]: pass

    @abstractmethod
    def train_with_examples(self): pass

    @abstractmethod
    async def train_with_data_ref_async(self): pass
