# README.md

## Project Overview

This project is a Python application that fetches and visualizes data from NASA's Near Earth Object (NEO) API. The application retrieves data about a specific NEO by its ID, cleans the data, and then visualizes the distance of the NEO over time.

## Dependencies

The project uses several Python libraries, which are listed in the `requirements.txt` file. These include:

- `requests` for making HTTP requests to the NASA API.
- `pandas` for data manipulation and analysis.
- `matplotlib` for data visualization.

## How to Run the Program

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Run the `main.py` script. This script fetches the NEO data, cleans it, and visualizes it.

## Code Overview

The code is organized into two Python files:

- `neo_lib.py`: This file contains three functions:
  - `get_neo_data(neo_id, api_key)`: Fetches the NEO data from the NASA API.
  - `clean_neo_data(df)`: Cleans the fetched data by converting dates to datetime format, sorting the data by dates, and converting distances to float.
  - `visualize_neo_data(df)`: Visualizes the cleaned data using a line plot.

- `main.py`: This is the main script that uses the functions from `neo_lib.py` to fetch, clean, and visualize the NEO data.

## Data Visualization

The data visualization is a line plot that shows the distance of the NEO over time. The x-axis represents the dates of the NEO's close approaches, and the y-axis represents the distance of the NEO in miles. The distance is represented in millions of miles for readability.

## API Key

The NASA API requires an API key, which is currently set to "DEMO_KEY" in `main.py`. For more frequent requests, you should obtain a personal API key from NASA's API portal.