#This Script is to Operate Auto Car Simulation
import sys

DIRECTIONS = ["N", "E", "S", "W"]

class Car:
    def __init__(self, name, x, y, direction, commands):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = list(commands)
        self.active = True 

    def Car_Rotate_Left(self):
        idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(idx - 1) % 4]

    def Car_Rotate_Right(self):
        idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(idx + 1) % 4]

    def Move_Forward(self, width, height):
        dx, dy = 0, 0
        if self.direction == "N":
            dy = 1
        elif self.direction == "S":
            dy = -1
        elif self.direction == "E":
            dx = 1
        elif self.direction == "W":
            dx = -1

        new_x, new_y = self.x + dx, self.y + dy
        if 0 <= new_x < width and 0 <= new_y < height:
            self.x, self.y = new_x, new_y
        

    def execute_command(self, cmd, width, height):
        if cmd == "L":
            self.Car_Rotate_Left()
        elif cmd == "R":
            self.Car_Rotate_Right()
        elif cmd == "F":
            self.Move_Forward(width, height)

    def __str__(self):
        return f"{self.name}, ({self.x},{self.y}) {self.direction}"


class Simulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def run(self):
        max_steps = max(len(c.commands) for c in self.cars)
        for step in range(max_steps):
            positions = {}
            for car in self.cars:
                if not car.active or step >= len(car.commands):
                    continue
                car.execute_command(car.commands[step], self.width, self.height)
                pos = (car.x, car.y)
                if pos in positions:
                    
                    other = positions[pos]
                    car.active = False
                    other.active = False
                    print(f"- {car.name}, collides with {other.name} at {pos} at step {step+1}")
                    print(f"- {other.name}, collides with {car.name} at {pos} at step {step+1}")
                else:
                    positions[pos] = car

        # Print the final results for non-collided cars
        for car in self.cars:
            if car.active:
                print(f"- {car}")


def main():
    print("Welcome to Auto  Driving Car Simulation!\n")
    width, height = map(int, input("Please enter the width and height of the car simulation field in x y format:\n").split())
    sim = Simulation(width, height)
    print(f"You have created a field of {width} x {height}.\n")

    while True:
        print("Please choose  from the following options:\n[1] Add a car to field\n[2] Run simulation")
        choice = input().strip()
        if choice == "1":
            name = input("Please enter the name of the car:\n").strip()
            x, y, direction = input(f"Please enter  intial position of car {name} in x y Direction format:\n").split()
            x, y = int(x), int(y)
            commands = input(f"Please enter the commands for car {name}:\n").strip()
            car = Car(name, x, y, direction, commands)
            sim.add_car(car)
            print("\nYour current list of cars are:")
            for c in sim.cars:
                print(f"- {c.name}, ({c.x},{c.y}) {c.direction}, {''.join(c.commands)}")
        elif choice == "2":
            print("\nYour current list of cars are:")
            for c in sim.cars:
                print(f"- {c.name}, ({c.x},{c.y}) {c.direction}, {''.join(c.commands)}")
            print("\nAfter simulation, the result is:")
            sim.run()
            print("\nPlease choose  from the following options:\n[1] Start over\n[2] Exit")
            post = input().strip()
            if post == "1":
                return main()
            else:
                print("Thank you for running the Car simulation. Goodbye!")
                sys.exit()


if __name__ == "__main__":
    main()