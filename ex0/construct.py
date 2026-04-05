import sys
import os

if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\nScripts")
        print("activate     # On Windows")
        print("\nThen run this program again.")

    if sys.prefix != sys.base_prefix:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        venv_path = os.environ.get("VIRTUAL_ENV")
        venv_name = venv_path.split("/")[-1]
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.\n")
        print("Package installation path:")
        print(sys.path)