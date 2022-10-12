from . import MLSourceCredential, DataSourceCredential

class MLSourceDefinition:
    ml_src_credential: MLSourceCredential
    ml_src_parameters: dict(str, str)

class DataSourceDefinition:
    data_src_credential: DataSourceCredential
    data_src_parameters: dict(str, str)