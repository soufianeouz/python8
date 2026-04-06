import importlib

print("\nLOADING STATUS: Loading programs...\n")
print("Checking dependencies:")

# modules = ["pandas", "numpy", "requests", "matplotlib"]
modules = {
    "pandas": " Data manipulation ready",
    "numpy": " Numerical computation ready",
    "requests": " Network access ready",
    "matplotlib": " Visualization ready"
}

for key, value in modules.items():
    try:
        module = importlib.import_module(key)
        print(f"[OK] {key} ({module.__version__})- {value}")
    except ModuleNotFoundError as e:
        print(f"[ERROR], {e}")