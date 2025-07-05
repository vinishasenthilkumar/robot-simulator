# test_robot.py

import unittest
from robot import Terrain

class TestRobotMovement(unittest.TestCase):
    def setUp(self):
        self.terrain = Terrain()
        self.terrain.create_robot("A")
        self.terrain.create_robot("B")

    def test_initial_position(self):
        self.assertEqual(self.terrain.get_robot_position("A"), (0, 0))
        self.assertEqual(self.terrain.get_robot_position("B"), (0, 0))

    def test_movement_east(self):
        self.terrain.move_robot("A", "E2")
        self.assertEqual(self.terrain.get_robot_position("A"), (2, 0))

    def test_collision_avoidance(self):
        self.terrain.move_robot("A", "E3")
        self.terrain.move_robot("B", "E5")
        self.assertEqual(self.terrain.get_robot_position("B"), (2, 0)) 

    def test_invalid_command(self):
        with self.assertRaises(ValueError):
            self.terrain.move_robot("A", "Z5")

    def test_invalid_robot(self):
        with self.assertRaises(ValueError):
            self.terrain.move_robot("X", "E2")

if __name__ == '__main__':
    unittest.main()
