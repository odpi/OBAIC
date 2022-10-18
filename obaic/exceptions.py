
class DataSourceAuthenticationError(Exception):
    """
    Raised when connection to a datasource failed authentication.
    """
    
    pass

class MLSourceAuthenticationError(Exception):
    """
    Raised when connection to a ML source failed authentication.
    """
    
    pass

class RequestTimeoutError(Exception):
    """
    Raised when a OBAIC request exceeded timeout
    """
    
    pass

class MLSourceError(Exception):
    """
    Raised when an error occured while processing a request at ML source.
    """
    
    pass

class DataSourceError(Exception):
    """
    Raised when an error occured while processing a request at the data source.
    """
    
    pass
