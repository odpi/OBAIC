from collections.abc import Iterable
from obaic import obaic
from obaic.model import ObaicModel
from obaic.requests import ObaicModelQuery, PredictionRequest
from obaic.source import MLSource
from obaic.sourcedefinitions import MLSourceDefinition

# define an ML source where predictions will be done
mlSourceDefn: MLSourceDefinition = MLSourceDefinition()

# connect to the ML source
mlSource: MLSource = MLSource(mlSourceDefn)
mlSource.connect()

# define a model query and fetch a list of models from the ML source
modelQuery: ObaicModelQuery = ObaicModelQuery()
mlModels: Iterable[ObaicModel] = mlSource.list_models(modelQuery)

# pick a model from the list mlModels using some criteria
mlModel: ObaicModel

# define a prediction request and run a prediction using the model selected above
predictionRequest: PredictionRequest = PredictionRequest()
mlScore: ObaicScore = mlSource.predict(mlModel, predictionRequest)