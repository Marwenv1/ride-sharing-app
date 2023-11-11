
class RideScheduleException(Exception):
    """Exception raised for errors in the scheduling of rides."""
    def __init__(self, message="Error with ride scheduling"):
        self.message = message
        super().__init__(self.message)
