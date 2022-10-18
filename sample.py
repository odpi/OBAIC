from collections.abc import Iterable

from obaic.model import ObaicModel
from obaic.requests import ObaicModelQuery, PredictionRequest
from obaic.responses import ObaicOutput
from obaic.source import MLSource
from obaic.sourcedefinitions import MLSourceDefinition

def main():

    # define an ML source where predictions will be done
    ml_src_defn: MLSourceDefinition = MLSourceDefinition()

    # connect to the ML source
    ml_src: MLSource = MLSource(ml_src_defn)

    # 1. define a model query and fetch a list of models from the ML source
    model_query: ObaicModelQuery = ObaicModelQuery()
    ml_model_iter: Iterable[ObaicModel] = ml_src.list_models(model_query)

    # 3. pick a model from the list mlModels using some criteria
    for ml_model in ml_model_iter:
        if ml_model : # check for some criteria
            select_ml_model = ml_model
            break

    # 4. define a prediction request and run a prediction using the model selected above
    prediction_req: PredictionRequest = PredictionRequest()
    prediction_response: list[ObaicOutput] = ml_src.predict(select_ml_model, prediction_req)
