class Elevator:
    def __init__(self, id, max_floor, min_floor=0):
        self.id = id
        self.current_floor = 0
        self.direction = "UP"  # "UP" or "DOWN"
        self.max_floor = max_floor
        self.min_floor = min_floor
        self.requests = []

    def add_request(self, floor):
        if self.min_floor <= floor <= self.max_floor:
            self.requests.append(floor)
            print(f"Request to floor {floor} added.")
        else:
            print(f"Invalid floor request: {floor}.")

    def move(self):
        while self.requests:
            next_floor = self.requests.pop(0)
            self._move_to_floor(next_floor)
    
    def _move_to_floor(self, floor):
        if floor > self.current_floor:
            self.direction = "UP"
        elif floor < self.current_floor:
            self.direction = "DOWN"
        
        print(f"Moving {self.direction} to floor {floor}...")
        self.current_floor = floor
        print(f"Elevator {self.id} arrived at floor {floor}.")

