import sys
missing = []

lib = ["numpy", "pandas", "matplotlib"]
for pkg in lib:
    try:
        __import__(pkg)
    except ImportError:
        missing.append(pkg)

if missing:
    for pkg in missing:
        print(f"{pkg} IS NOT INSTALLED. - use: pip install {pkg}")
    sys.exit(1)

import importlib.metadata
import numpy
import pandas
import matplotlib.pyplot as plt


def check_dependencies() -> None:
    dependencies_list = ["pandas", "numpy", "matplotlib"]
    for pkg in dependencies_list:
        try:
            version = importlib.metadata.version(pkg)
            if pkg == "pandas":
                print(f"[OK] {pkg} ({version}) - Data manipulation ready")
            elif pkg == "numpy":
                print(f"[OK] {pkg} ({version}) - Numerical computation ready")
            elif pkg == "matplotlib":
                print(f"[OK] {pkg} ({version}) - Visualization ready")
        except importlib.metadata.PackageNotFoundError:
            print(f"[KO] {pkg} - NOT INSTALLED")
    print()


def visualize(df: pandas.DataFrame) -> None:
    counts = df["signal"].value_counts()

    plt.figure(figsize=(8, 4))

    plt.bar(
        counts.index.astype(str),
        counts.to_numpy()
    )

    plt.xlabel("Value")
    plt.ylabel("Count")
    plt.title("Data Visualization")

    plt.savefig("matrix_analysis.png")


def picture_generator() -> None:
    print("\nLOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")
    check_dependencies()

    data = numpy.random.choice([1, 5, 10, 20], 1000)

    df = pandas.DataFrame({
        "signal": data,
        "time": numpy.arange(len(data))
    })
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...\n")

    visualize(df)

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    picture_generator()
