class Floor:
    def __init__(self, number):
        self.number = number
        self.up_requests = []
        self.down_requests = []

    def request_up(self, elevator, floor_number):
        print(f"Requesting elevator to go UP from floor {self.number} to {floor_number}")
        elevator.add_request(floor_number)

    def request_down(self, elevator, floor_number):
        print(f"Requesting elevator to go DOWN from floor {self.number} to {floor_number}")
        elevator.add_request(floor_number)
