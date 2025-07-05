# main.py

from robot import RobotSimulator

def main():
    simulator = RobotSimulator()

    simulator.add_robot("R1")
    simulator.add_robot("R2")

    simulator.issue_command("R1", "E3")
    print(f"R1: {simulator.get_robot_current_position('R1')}")

    simulator.issue_command("R2", "E5")
    print(f"R2: {simulator.get_robot_current_position('R2')}")

    simulator.issue_command("R1", "N2")
    print(f"R1: {simulator.get_robot_current_position('R1')}")

    simulator.issue_command("R2", "E1")
    print(f"R2: {simulator.get_robot_current_position('R2')}")

if __name__ == "__main__":
    main()
