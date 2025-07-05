# robot.py

class Robot:
    def __init__(self, robot_id):
        self.robot_id = robot_id
        self.x = 0
        self.y = 0

    def get_position(self):
        return (self.x, self.y)

    def move(self, direction, steps, occupied_cells):
        dx, dy = 0, 0

        if direction == 'N':
            dy = 1
        elif direction == 'S':
            dy = -1
        elif direction == 'E':
            dx = 1
        elif direction == 'W':
            dx = -1
        else:
            raise ValueError(f"Invalid direction: {direction}")

        for _ in range(steps):
            next_x = self.x + dx
            next_y = self.y + dy

            if (next_x, next_y) in occupied_cells:
                break  

            self.x = next_x
            self.y = next_y


class Terrain:
    def __init__(self):
        self.robots = {}

    def create_robot(self, robot_id):
        if robot_id in self.robots:
            raise ValueError(f"Robot with ID {robot_id} already exists.")
        self.robots[robot_id] = Robot(robot_id)

    def get_robot_position(self, robot_id):
        self._check_robot_exists(robot_id)
        return self.robots[robot_id].get_position()

    def move_robot(self, robot_id, command):
        self._check_robot_exists(robot_id)

        if len(command) < 2:
            raise ValueError("Invalid command format")

        direction = command[0].upper()
        try:
            steps = int(command[1:])
        except ValueError:
            raise ValueError("Step count must be a number")

        occupied = {
            robot.get_position()
            for rid, robot in self.robots.items()
            if rid != robot_id
        }

        self.robots[robot_id].move(direction, steps, occupied)

    def _check_robot_exists(self, robot_id):
        if robot_id not in self.robots:
            raise ValueError(f"Robot with ID {robot_id} does not exist.")
