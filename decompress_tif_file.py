import matplotlib.pyplot as plt  
import os 
import rasterio  

# Get paths of TIFF files in a folder
def get_tiff_files(folder_path):
    # List to store paths of TIFF files
    tiff_files = []  
    
    for root, dirs, files in os.walk(folder_path):  
        for file in files:  
            if file.endswith(".tiff") or file.endswith(".tif"):  # Check if file is TIFF
                file_path = os.path.join(root, file)  # Get full path of TIFF file
                if os.path.getsize(file_path) > 200 * 1024:  # Check if file size is greater than 200 KB
                    tiff_files.append(file_path) 
    return tiff_files 

# Plot bands from a TIFF file
def plt_tif_file(tiff_path, bands, save_path):
    with rasterio.open(tiff_path) as src:  # Open TIFF file
        img = src.read()  # Read image data
        num_bands = img.shape[0]  

        nrows = num_bands  
        ncols = 1  

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(20, 8 * nrows))  # Create subplots

        for i in range(num_bands): 
            band = img[i]  # Get band data

            height, width = band.shape  

            title = f'{bands[i]}'  

            axes[i].imshow(band)  
            axes[i].set_title(title) 
            axes[i].set_xlabel('X') 
            axes[i].set_ylabel('Y')  
             
        plt.tight_layout()  
        plt.savefig(save_path, bbox_inches='tight')  
        plt.show()  

# Date range
year = 2023
start_month = 1
end_month = 10
start_date = 1
end_date = 31

# Path to the folder containing TIFF files
path_load_tif = 'Path to load tif file' 

# List of bands
bands = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B8A', 'B9', 'B10', 'B11', 'B12']

for j in range(start_month, end_month + 1):
    if j < 10:
        month = f'0{j}' 
    else:
        month = j
    for i in range(start_date, end_date + 1):
        if i < 10:
            day = f'0{i}'
        else:
            day = i
        start = f'{year}-{month}-{day}'  
        end = f'{year}-{month}-{day}'  
        
        path = f'{path_load_tif}/{start}/'  # Path to the folder containing TIFF files for this date
        
        try:
            a = get_tiff_files(path)  # Get list of TIFF files in the folder
            a = a[0].replace("\\response.tiff'", "//response.tiff") 
            save_path = f'{path_load_tif}/{start}.png'  # Path to save the PNG file
            plt_tif_file(a, bands, save_path)  # Plot and save the bands as a PNG file
        except:
            pass