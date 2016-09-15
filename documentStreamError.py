class DocumentStreamError(Exception):
    """
    This class inherits from the Exception class to handle potential errors
    from the class DocumentStream.
    """
    def __init__(self, message):
        self.data = message
