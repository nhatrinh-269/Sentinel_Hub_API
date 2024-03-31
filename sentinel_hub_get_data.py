from sentinelhub import (  
    CRS,
    BBox, 
    DataCollection,
    MimeType,
    MosaickingOrder,  
    SentinelHubRequest,  
    bbox_to_dimensions,  
    SHConfig  
)

def sentinel(id_, client_secret_, lat_lng, evalscript_, start_time, end_time, path_save):
    """
    Fetches satellite imagery data using Sentinel Hub API.
    
    Parameters:
    - id_ (str): Your Sentinel Hub OAuth client ID.
    - client_secret_ (str): Your Sentinel Hub OAuth client secret.
    - lat_lng (tuple): Latitude and longitude coordinates defining the area of interest.
    - evalscript_ (str): Evaluation script for data processing.
    - start_time (str): Start date of the time interval for data retrieval (format: 'YYYY-MM-DD').
    - end_time (str): End date of the time interval for data retrieval (format: 'YYYY-MM-DD').
    - path_save (str): Path to save the retrieved imagery data.
    """

    id = id_ 
    client_secret = client_secret_  
    
    # Configure Sentinel Hub API access
    config = SHConfig()  # Create a configuration object
    config.sh_client_id = id  # Set OAuth client ID
    config.sh_client_secret = client_secret  # Set OAuth client secret

    if not config.sh_client_id or not config.sh_client_secret: 
        print("Warning! To use Process API, please provide the credentials (OAuth client ID and client secret).")
        
    # Define area of interest
    _coords_wgs84 = lat_lng  
    resolution = 1  
    _bbox = BBox(bbox=_coords_wgs84, crs=CRS.WGS84)  # Create a BBox object
    _size = bbox_to_dimensions(_bbox, resolution=resolution)  # Calculate dimensions from BBox
    
    # Define evaluation script and request parameters
    evalscript_all_bands = evalscript_  

    # Create a Sentinel Hub request object
    request_all_bands = SentinelHubRequest( 
            data_folder=path_save,  
            evalscript=evalscript_all_bands,  

            # Input data for the request
            input_data=[  
                SentinelHubRequest.input_data(
                    data_collection=DataCollection.SENTINEL2_L1C,  # Sentinel-2 Level-1C data collection
                    time_interval=(start_time, end_time), 
                    mosaicking_order=MosaickingOrder.LEAST_RECENT,  # Mosaicking order for overlapping images
                )
            ],
            responses=[SentinelHubRequest.output_response("default", MimeType.TIFF)],  # Output response format
            bbox=_bbox,  # Bounding box
            size=_size,  # Image dimensions
            config=config,  # Configuration object
        )
    
    # Get and save the data
    all_bands_response = request_all_bands.get_data()  # Retrieve data
    all_bands_img = request_all_bands.get_data(save_data=True)  # Retrieve and save data
    return
    
evalscript_all_bands = """
    //VERSION=3  # Version of the evaluation script

    // Function to setup input and output parameters
    function setup() {
        return {
            input: [{
                bands: ["B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08", "B8A", "B09", "B10", "B11", "B12"],  # Input bands
                units: "DN"  # Data unit
            }],
            output: {
                bands: 13,  # Number of output bands
                sampleType: "INT16"  # Sample type
            }
        };
    }

    // Function to evaluate pixel values
    function evaluatePixel(sample) {
        return [sample.B01,  # Return pixel values for each band
                sample.B02,
                sample.B03,
                sample.B04,
                sample.B05,
                sample.B06,
                sample.B07,
                sample.B08,
                sample.B8A,
                sample.B09,
                sample.B10,
                sample.B11,
                sample.B12];
    }
"""  

# Sentinel Hub OAuth credentials
id = 'Your Sentinel Hub OAuth client ID'  # Replace with your client ID
client_secret = 'Your Sentinel Hub OAuth client secret'  # Replace with your client secret

# Coordinates and resolution
betsiboka_coords_wgs84 = (107.85459547384416, 14.50270988907517, 107.87605314634027, 14.51162173005985)
resolution = 1

# Date range
year = 2023
start_month = 1
end_month = 10
start_date = 1
end_date = 31

path_save_tif = 'Path to save the retrieved imagery data'

# Loop through each day in the specified date range
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
        path = f'{path_save_tif}/{start}/'  
        try:
            sentinel(id, client_secret, betsiboka_coords_wgs84, evalscript_all_bands, start, end, path)
            print(f'{start}has been loaded')  
        except:
            print(f'{start} was faulty')  
