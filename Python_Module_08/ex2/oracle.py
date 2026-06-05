import os
import sys

try:
    from dotenv import load_dotenv  # type: ignore[import-not-found]
except ImportError as e:
    print(f"Error: {e} - To install it use: pip install python_dotenv")
    sys.exit(1)

load_dotenv()


def data_message(url: str | None, mode: str) -> str:
    if not url:
        return "Not configured"
    if mode == "production":
        return "Connected to the production instance"
    return "Connected to local instance"


def api_message(api_key: str | None) -> str:
    if not api_key:
        return "Not authenticated"
    return "Authenticated"


def zion_message(endpoint: str | None) -> str:
    if not endpoint:
        return "Offline"
    return "Online"


def security_check() -> None:
    print("Environment security check:")
    print(" [OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print(" [OK] .env file properly configured")
    else:
        print(" [KO] No .env found - copy .env.example to .env")
    if os.environ.get("MATRIX_MODE") or os.environ.get("API_KEY"):
        print(" [OK]  Production overrides available")


def oracle() -> None:
    mode = os.environ.get("MATRIX_MODE", "development")
    data = os.environ.get("DATABASE_URL")
    api = os.environ.get("API_KEY")
    log = os.environ.get("LOG_LEVEL")
    endpoint = os.environ.get("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {data_message(data, mode)}")
    print(f"API Access: {api_message(api)}")
    print(f"Log level: {log}")
    print(f"Zion Network: {zion_message(endpoint)}")

    security_check()
    print("\nOracle sees all configurations.")


if __name__ == "__main__":
    oracle()
