from Elevator import Elevator
from Floor import Floor

class ElevatorController:
    def __init__(self, num_floors, num_elevators):
        self.num_floors = num_floors
        self.num_elevators = num_elevators
        self.elevators = [Elevator(id=i, max_floor=num_floors-1) for i in range(num_elevators)]
        self.floors = [Floor(i) for i in range(num_floors)]

    def handle_request(self, elevator_id, target_floor):
        if 0 <= elevator_id < self.num_elevators:
            elevator = self.elevators[elevator_id]
            elevator.add_request(target_floor)
        else:
            print(f"Invalid elevator ID: {elevator_id}")

    def run_elevators(self):
        for elevator in self.elevators:
            print(f"Starting Elevator {elevator.id}...")
            elevator.move()
