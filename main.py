# main.py

from robot import Terrain

def main():
    terrain = Terrain()

    terrain.create_robot("R1")
    terrain.create_robot("R2")

    terrain.move_robot("R1", "E3")
    print(f"R1: {terrain.get_robot_position('R1')}")  

    terrain.move_robot("R2", "E5")  
    print(f"R2: {terrain.get_robot_position('R2')}")  

    terrain.move_robot("R1", "N2")
    print(f"R1: {terrain.get_robot_position('R1')}")  

    terrain.move_robot("R2", "E1")
    print(f"R2: {terrain.get_robot_position('R2')}")  

if __name__ == "__main__":
    main()
