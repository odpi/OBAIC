from typing import Any, Optional

class Credential:
    """
    Implementations support one or more of the following
    Anonymous, Basic, Token, X509, Key file
    """
    type: str
    username: Optional[str]
    password: Optional[str]
    token: Optional[str]
    path: Optional[str]

class MLSourceCredential(Credential): 
    """
    Credentials to ML engine
    """

    pass

class DataSourceCredential(Credential):
    """
    Credentials to data source
    """
    pass