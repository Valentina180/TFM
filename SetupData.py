import os
import zipfile
from dotenv import load_dotenv
from kaggle.api.kaggle_api_extended import KaggleApi

# 1. Load credentials from .env
load_dotenv()

def download_and_unzip():
    # 2. Authenticate with Kaggle
    api = KaggleApi()
    api.authenticate()

    dataset = "aptos2019-blindness-detection"
    # Define the data folder path
    data_dir = "data"
    
    # Create the 'data' folder if it doesn't exist yet
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created directory: {data_dir}")

    # 3. Download the competition files directly into the data folder
    print(f"Downloading {dataset} into {data_dir}/...")
    # 'path' tells Kaggle where to put the downloaded zip
    api.competition_download_files(dataset, path=data_dir)

    # The file Kaggle creates will be inside the data folder
    zip_file_path = os.path.join(data_dir, f"{dataset}.zip")

    # 4. Unzip using Python
    if os.path.exists(zip_file_path):
        print(f"Unzipping {zip_file_path}...")
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # Extracting into the same data folder
            zip_ref.extractall(data_dir)
        
        # Remove the zip file to keep the 'data' folder clean
        os.remove(zip_file_path) 
        print(f"Done! Files are ready in the '{data_dir}' folder.")
    else:
        print("Error: Download failed. Check your Kaggle credentials and rules acceptance.")

if __name__ == "__main__":
    download_and_unzip()