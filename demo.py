import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from constant.enums import get_user_type_name

if __name__ == "__main__":
    print("User type for ID 2 is:", get_user_type_name(2))
    name = os.getenv("name", "default_name") 
    print(f"Name from Environment.., {name}!")
    user_id=get_user_type_name(2)
    name=os.getenv("name", "default_name")
    os.makedirs("output", exist_ok=True)
    with open("output/demo_output.txt", "w") as f:
        f.write(f"User type for ID 2 is: {user_id}\n")
        f.write(f"Name from Environment: {name}\n")
