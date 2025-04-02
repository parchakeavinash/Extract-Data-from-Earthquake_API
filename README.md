# Earthquake Data Fetcher

## Overview
This Python script fetches earthquake data from the USGS (United States Geological Survey) API for the past 15 days and saves it as a CSV file. The data includes details such as location, magnitude, depth, and time of occurrence.

## Features
- Retrieves earthquake data from the USGS API.
- Extracts relevant earthquake information.
- Saves the data in CSV format.

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install requests pandas
```

## Usage
1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/earthquake-data-fetcher.git
   cd earthquake-data-fetcher
   ```

2. Run the script:

   ```bash
   python earthquake_fetcher.py
   ```

3. The output CSV file will be saved in the specified directory (`C:/Users/BP/Downloads/python code converter/`), with the filename format `earthquake_data_YYYY-MM-DD.csv`.

## Script Details
The script:
- Determines the current date and calculates the date 15 days prior.
- Constructs the API URL with the required date range.
- Fetches earthquake data in JSON format.
- Extracts essential details such as magnitude, place, time, latitude, longitude, and depth.
- Saves the data in a CSV file.

## Example Output
A sample of the CSV file format:

| Place | Magnitude | Time | Latitude | Longitude | Depth |
|-------|----------|------|----------|-----------|-------|
| California | 4.5 | 2025-03-15 10:30:00 | 36.7783 | -119.4179 | 10 |

## Notes
- Ensure an active internet connection to fetch data.
- The output file location can be modified in the script as needed.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Avinash Parchake

---

Feel free to modify the script or customize the README as needed!

