import pandas as pd

def analyze_csv():
    file = input("Enter CSV file path: ")
    try:
        df = pd.read_csv(file)
        print("\n✅ Data Loaded Successfully!\n")
        print("First 5 rows:\n", df.head())
        print("\nSummary statistics:\n", df.describe())
        print("\nColumns:", list(df.columns))
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    analyze_csv()
