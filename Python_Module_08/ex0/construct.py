import sys
import os


def construct() -> None:
    path = sys.executable
    venv = os.environ.get("VIRTUAL_ENV")
    if venv:
        venv_name = os.path.basename(venv)
        package_path = os.path.join(
            venv,
            f"lib/python/{sys.version[:6]}",
            "site-packages")
        print()
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {path}")
        print(f"Virtual Environment: {venv_name}\n")
        print(f"Environment Path: {venv}")
        print("SUCCESS: You're in an isolated environment!\n\
Safe to install packages without affecting the global system.")
        print(f"Package installation path:\n\
{package_path}")
    else:
        print()
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {path}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")

    sys.exit(0)


if __name__ == "__main__":
    construct()
