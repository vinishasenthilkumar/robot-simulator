# test_robot.py

import unittest
from robot import RobotSimulator 

class TestRobotSimulation(unittest.TestCase):
    def setUp(self):
        self.simulator = RobotSimulator()
        self.simulator.add_robot("A")
        self.simulator.add_robot("B")

    def test_initial_robot_placement(self):
        self.assertEqual(self.simulator.get_robot_current_position("A"), (0, 0))
        self.assertEqual(self.simulator.get_robot_current_position("B"), (0, 0))

    def test_movement_east(self):
        self.simulator.issue_command("A", "E2")
        self.assertEqual(self.simulator.get_robot_current_position("A"), (2, 0))

    def test_collision_prevention(self):
        self.simulator.issue_command("A", "E3")
        self.simulator.issue_command("B", "E5")
        self.assertEqual(self.simulator.get_robot_current_position("B"), (2, 0))

    def test_invalid_command_format(self):
        with self.assertRaises(ValueError):
            self.simulator.issue_command("A", "Z5") 

    def test_invalid_robot(self):
        with self.assertRaises(ValueError):
            self.simulator.issue_command("X", "E2") 


if __name__ == '__main__':
    unittest.main()
