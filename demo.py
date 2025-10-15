import sys
import os


if __name__ == "__main__":
    print("hello world")
    name = os.getenv("name", "default_name") 
    print(f"Name from Environment.., {name}!")
    os.makedirs("output", exist_ok=True)
    with open("output/demo_output.txt", "w") as f:
        f.write(f"Name from Environment: {name}\n")
