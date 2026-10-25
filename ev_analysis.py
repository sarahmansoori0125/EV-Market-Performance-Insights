
import pandas as pd

# Load the electric vehicle dataset
file_path = "open-ev-data-v1.24.0.csv"
df = pd.read_csv(file_path)

print("ELECTRIC VEHICLE MARKET ANALYSIS")
print("-" * 40)

# Dataset overview
print("\nDataset Shape:")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nColumn Names:")
print(df.columns.tolist())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum().sort_values(ascending=False).head(10))

# Summarize manufacturers
if "Make Name" in df.columns:
    print("\nTop 10 Manufacturers by Number of Records:")
    print(df["Make Name"].value_counts().head(10))

# Average battery capacity
if "Battery Capacity Net Kwh" in df.columns:
    print("\nAverage Net Battery Capacity (kWh):")
    print(pd.to_numeric(
        df["Battery Capacity Net Kwh"], errors="coerce"
    ).mean())

# Average motor power
if "Ac Max Power Kw" in df.columns:
    print("\nAverage Maximum Power (kW):")
    print(pd.to_numeric(
        df["Ac Max Power Kw"], errors="coerce"
    ).mean())

# Save a summary of the dataset
df.describe(include="all").to_csv("ev_analysis_summary.csv")

print("\nAnalysis complete. Summary saved to ev_analysis_summary.csv")
