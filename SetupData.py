import os
import zipfile
from dotenv import load_dotenv
from kaggle.api.kaggle_api_extended import KaggleApi

# 1. Load credentials from .env
load_dotenv()

def download_and_unzip():
    # 2. Authenticate with Kaggle
    # The library automatically looks for KAGGLE_USERNAME and KAGGLE_KEY in env variables
    api = KaggleApi()
    api.authenticate()

    dataset = "aptos2019-blindness-detection"
    zip_file = f"{dataset}.zip"
    extract_path = "data/"

    # 3. Download the competition files
    print(f"Downloading {dataset}...")
    api.competition_download_files(dataset, path='.')

    # 4. Unzip using Python (cross-platform)
    if os.path.exists(zip_file):
        print(f"Unzipping {zip_file} into {extract_path}...")
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        
        # Optional: Remove the zip file to save space
        # os.remove(zip_file) 
        print("Done!")
    else:
        print("Error: Download failed. Check your Kaggle credentials and internet.")

if __name__ == "__main__":
    download_and_unzip()