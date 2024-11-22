from ElevatorController import ElevatorController

def main():
    # Initialize an elevator system with 10 floors and 2 elevators
    controller = ElevatorController(num_floors=10, num_elevators=2)
    
    # Simulate requests
    controller.handle_request(elevator_id=0, target_floor=3)
    controller.handle_request(elevator_id=1, target_floor=5)
    controller.handle_request(elevator_id=0, target_floor=7)
    
    # Run elevators to process requests
    controller.run_elevators()

if __name__ == "__main__":
    main()
