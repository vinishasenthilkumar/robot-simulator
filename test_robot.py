class Robot:
    def __init__(self, robot_id):
        self.robot_id = robot_id
        self.x_coord = 0
        self.y_coord = 0

    def get_current_position(self):
        return (self.x_coord, self.y_coord)

    def advance(self, direction, steps, occupied_coordinates):
        delta_x, delta_y = 0, 0

        if direction == 'N':
            delta_y = 1
        elif direction == 'S':
            delta_y = -1
        elif direction == 'E':
            delta_x = 1
        elif direction == 'W':
            delta_x = -1
        else:
            raise ValueError(f"Invalid direction: {direction}")

        for _ in range(steps):
            next_x = self.x_coord + delta_x
            next_y = self.y_coord + delta_y

            if (next_x, next_y) in occupied_coordinates:
                break

            self.x_coord = next_x
            self.y_coord = next_y


class RobotSimulator:
    def __init__(self):
        self.robots = {}

    def add_robot(self, robot_id):
        if robot_id in self.robots:
            raise ValueError(f"Robot with ID {robot_id} already exists.")
        self.robots[robot_id] = Robot(robot_id)

    def get_robot_current_position(self, robot_id):
        self._validate_robot_exists(robot_id)
        return self.robots[robot_id].get_current_position()

    def issue_command(self, robot_id, command):
        self._validate_robot_exists(robot_id)

        if len(command) < 2:
            raise ValueError("Invalid command format")

        move_direction = command[0].upper()
        try:
            num_steps = int(command[1:])
        except ValueError:
            raise ValueError("Step count must be a number")

        current_occupied_cells = {
            robot.get_current_position()
            for rid, robot in self.robots.items()
            if rid != robot_id
        }

        self.robots[robot_id].advance(move_direction, num_steps, current_occupied_cells)

    def _validate_robot_exists(self, robot_id):
        if robot_id not in self.robots:
            raise ValueError(f"Robot with ID {robot_id} does not exist.")
