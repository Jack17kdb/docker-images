import platform
import os

def get_system_info():
    print("🔹 Python Docker System Info 🔹")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Current Working Directory: {os.getcwd()}")
    print(f"Files in directory: {os.listdir('.')}")

if __name__ == "__main__":
    get_system_info()
