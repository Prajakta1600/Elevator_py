class Request:
    def __init__(self, requested_floor):
        self.requested_floor = requested_floor

    def __repr__(self):
        return f"Request to floor {self.requested_floor}"
