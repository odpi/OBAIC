from collections.abc import Iterable
from typing import List, Dict

from obaic.model import ObaicModel
from obaic.source import MLSource, ObaicFeature, ObaicOutput

def main():

    ml_src_parameters: Dict[str, str]
    ml_src_credentials: Dict[str, str]

    # define an ML source where predictions will be done
    ml_src: MLSource = MLSource(ml_src_parameters=ml_src_parameters,
                                ml_src_credentials=ml_src_credentials)

    # 1. define a model query and fetch a list of models from the ML source
    model_query: str
    ml_model_iter: Iterable[ObaicModel] = ml_src.list_models(model_query=model_query)

    # 3. pick a model from the list mlModels using some criteria
    for ml_model in ml_model_iter:
        if ml_model : # check for some criteria
            select_ml_model = ml_model
            break

    features: List[ObaicFeature] 
    # 4. define a prediction request and run a prediction using the model selected above
    prediction_response: List[ObaicOutput] = ml_src.predict_with_features(model=select_ml_model, features=features)
