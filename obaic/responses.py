from typing import Optional, ABCMeta

class ObaicResponse(metaclass=ABCMeta): pass

class ModelResponse(ObaicResponse): pass

class PredictionResponse(ObaicResponse): pass