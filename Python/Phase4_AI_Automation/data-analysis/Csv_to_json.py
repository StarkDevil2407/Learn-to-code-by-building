import pandas as pd
import json

def csv_to_json(csv_file, json_file):
    try:
        df = pd.read_csv(csv_file)
        df.to_json(json_file, orient="records", indent=4)
        print(f"✅ Converted {csv_file} to {json_file}")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    csv = input("Enter CSV file name: ")
    json_file = input("Enter output JSON file name: ")
    csv_to_json(csv, json_file)
