from collections.abc import Iterable
from mailcap import findmatch
from obaic import obaic
from obaic.model import ObaicModel
from obaic.source import MLSource, ObaicFeature, ObaicOutput

import asyncio

async def main():

    ml_src_parameters: dict[str, str]
    ml_src_credentials: dict[str, str]

    # define an ML source where predictions will be done
    ml_src: MLSource = MLSource(ml_src_parameters=ml_src_parameters, 
                                ml_src_credentials=ml_src_credentials)

    # 1. define a model query and fetch a list of models from the ML source
    model_query: str
    ml_model_iter: Iterable[ObaicModel] = ml_src.list_models_async(model_query=model_query)

    # 3. pick a model from the list mlModels using some criteria
    for ml_model in ml_model_iter:
        if ml_model : # check for some criteria
            select_ml_model = ml_model
            break

    # 4. define a prediction request and run a prediction using the model selected above
    data_src_parameters: dict[str,str]
    data_src_credentials: dict[str,str]
    data_query: str
    predict_task = asyncio.create_task(
                        ml_src.predict_with_data_ref_async(model=select_ml_model, 
                                                           data_src_parameters=data_src_parameters,
                                                           data_src_credentials=data_src_credentials,
                                                           data_query=data_query)
                    )
    await predict_task