class ObaicModelFormat:
    """
    PMML, ONNX, or other formats recognized by OBAIC
    """
    name: str
    version: str

class ObaicModelField:
    # source: http://dmg.org/pmml/v4-4/DataDictionary.html
    # name of the field
    name: str
    # admissible operations on the field
    # valid values are: categorical, ordinal, continuous
    op_type: str
    # data type of the field
    # valid values are: str, int, float, bool
    # date, time, datetime, datetime with timezone, etc.
    data_type: str
    # business meaning of the field
    taxonomy: str
    # example value
    example: str
    # whether null value is accepted
    allow_missing: bool
    # extra information like shape of data, distribution, min/max, etc.
    description: str

class ObaicModelFeature(ObaicModelField): pass

class ObaicModelOutput(ObaicModelField): pass

class ObaicModelMetric:
    # based on model used, metric can be 
    # accuracy, precision, recall, ROC,
    # AUC, Gini coefficient, Log loss, F1 score, MAE, MSE, etc.
    metric: str
    value: float

class ObaicModel:
    # A unique identifier for the model
    id: str
    # Name of the model
    name: str
    # Model revision
    revision: int
    format: ObaicModelFormat

    # source: https://en.wikipedia.org/wiki/Machine_learning
    # Artificial neural network | Decision trees |
    # Support-vector machines | Regression analysis |
    # Bayesian networks | Genetic algorithms | Proprietary
    algorithm: str
    
    # source: https://en.wikipedia.org/wiki/Machine_learning
    # pick one or more from the following list:
    # Agriculture | Banking | Computer vision |
    # Insurance | Machine translation | Marketing |
    # Anomaly detection | Handwriting recognition |
    # Natural language processing | Online advertising |
    # Recommender systems | Sentiment analysis |
    # Telecommunication | Time-series forecasting | etc.
    tags: set[str]
    dependency: str
    creator: str
    description: str
    example: list[ObaicModelFeature]
    prediction: list[ObaicModelOutput]
    performance: list[ObaicModelMetric]
    rating: int
    # link to the real model for download
    url: str