import importlib
import  sys

print("\nLOADING STATUS: Loading programs...\n")
print("Checking dependencies:")

modules = {
    "numpy": " Numerical computation ready",
    "pandas": " Data manipulation ready",
    "requests": " Network access ready",
    "matplotlib": " Visualization ready"
}

modules_to_imp = {}

for key, value in modules.items():
    try:
        module = importlib.import_module(key)
        print(f"[OK] {key} ({module.__version__})- {value}")
        modules_to_imp[key] = module
    except ModuleNotFoundError as e:
        print(f"[ERROR], {e}")
        sys.exit(1)

import numpy
import pandas
import matplotlib.pyplot as plt

print("\nAnalyzing Matrix data...")
print("Processing 1000 data points...")
data = numpy.random.rand(1000)
print("Generating visualization...")
df = pandas.DataFrame(data)
df.describe()

print()
# 3. Visualize
plt.hist(df[0], bins=50)
plt.title("Matrix Data Distribution")

print("Analysis complete!")
print("Results saved to: matrix_analysis.png")
# 4. Save
plt.savefig("matrix_analysis.png")
plt.close()