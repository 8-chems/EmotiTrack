import pandas as pd
import requests

def fetch_data(url: str) -> pd.DataFrame:
    response = requests.get(url)
    response.raise_for_status()
    return pd.DataFrame(response.json())

if __name__ == "__main__":
    data_url = "https://example.com/data"  # Replace with actual data source
    data = fetch_data(data_url)
    data.to_csv("data/raw/data.csv", index=False)
