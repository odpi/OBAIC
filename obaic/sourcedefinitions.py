from obaic import MLSourceCredential, DataSourceCredential
 
class MLSourceDefinition:
    """A class to represent the definition of an ML source 
    
    :type ml_src_credential: MLSourceCredential
    :param ml_src_credential:
        Credentials required to authenticated to an ML source

    :type ml_src_parameters: dict(str, str)
    :param ml_src_parameters:
        A dictionary that holds parameters needed to connect to an ML source
    """
    ml_src_credential: MLSourceCredential
    ml_src_parameters: dict(str, str)

class DataSourceDefinition:
    """A class to represent the definition of a data source 
    
    :type data_src_credential: DataSourceCredential
    :param data_src_credential:
        Credentials required to authenticated to a data source

    :type data_src_parameters: dict(str, str)
    :param data_src_parameters:
        A dictionary that holds parameters needed to connect to a data source
    """
    data_src_credential: DataSourceCredential
    data_src_parameters: dict(str, str)