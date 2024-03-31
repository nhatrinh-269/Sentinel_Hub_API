# Collect Timeseries Multispectral Satellite Images Using The Sentinel Hub API

## Overview
With the advancement of space satellite technology, accessing free satellite images for research and development has become more accessible. This repository provides an example of collecting time-series multispectral satellite imagery from Sentinel Hub using their API. The goal is to facilitate access to real-time multispectral satellite images for research purposes and monitoring changes on the Earth's surface over time.

## Files
### 1. `sentinel_hub_get_data.py`
This script defines a function named `sentinel()` responsible for retrieving time-series multispectral satellite imagery data from the Sentinel Hub API. It requires parameters such as OAuth client ID, client secret, coordinates of the region of interest, evaluation script for data processing, start and end dates for the data retrieval period, and the path to save the retrieved image data in TIFF format.

### 2. `decompress_tif_file.py`
This script utilizes the `get_tiff_files()` function to search for the downloaded TIFF files and extract them. It then employs the `plt_tif_file()` function to display the bands of the multispectral image.

## Dependencies
- `sentinelhub` Python package: Install using `pip install sentinelhub`.
- `rasterio` Python package: Install using `pip install rasterio`.
- `matplotlib` Python package: Install using `pip install matplotlib`.

## Usage
To use these scripts:
1. Replace the placeholders `'Your Sentinel Hub OAuth client ID'` and `'Your Sentinel Hub OAuth client secret'` in both scripts with your actual Sentinel Hub OAuth credentials.
2. Modify the `coordinates of the region of interest`, `evaluation script to process the data`, `start and end dates for the data retrieval period`, and `path to save retrieved image data` in `sentinel_hub_get_data.py` as per your requirements.
3. Run `sentinel_hub_get_data.py` to fetch the satellite imagery data.

## Access Sentinel Hub
To access Sentinel Hub, you can visit their website [here](https://www.sentinel-hub.com/). You will need to register and obtain your OAuth client ID and client secret to use their API.

## Note
Ensure that you provide correct credentials and configure the scripts according to your requirements before executing them. Additionally, make sure you have the necessary permissions and quota for accessing the Sentinel Hub API.
