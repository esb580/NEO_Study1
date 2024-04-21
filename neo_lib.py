import requests
import json
import pandas as pd
import matplotlib.pyplot as plt



def get_neo_data(neo_id, api_key):
    # Define the URL
    url = f"https://api.nasa.gov/neo/rest/v1/neo/{neo_id}?api_key={api_key}"

    # Make a get request to get the latest NEO data
    response = requests.get(url)

    # Convert the response data to a dictionary
    data = response.json()

    # Extract the distance in miles and dates from the response data
    distance_miles = []
    dates = []
    name = data['name']
    for close_approach_data in data['close_approach_data']:
        distance_miles.append(close_approach_data['miss_distance']['miles'])
        dates.append(close_approach_data['close_approach_date'])


    # Create a dictionary to store the extracted data
    neo_data = {
        'distance_miles': distance_miles,
        'dates': dates
    }

    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(neo_data)

    return df, name


# Define a function to clean the NEO data
def clean_neo_data(df):
    # Convert dates to datetime format
    df['dates'] = pd.to_datetime(df['dates'])

    # Sort DataFrame by dates
    df = df.sort_values('dates')

    # Convert distance to float with 2 decimal places
    df['distance_miles'] = df['distance_miles'].astype(float).round(2)

    return df


def visualize_neo_data(df, name):

    # Create a line plot
    plt.figure(figsize=(10, 6))
    plt.plot(df['dates'], df['distance_miles'], marker='o')

    # Set the title and labels
    plt.title('NEO Distance Over Time' + f' ({name})')
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    # create a list of yticks automatically based on the data
    yticks = list(range(0, int(df['distance_miles'].max()) + 1, 5000000))
    plt.yticks(yticks, [f'{y/1000000}M' for y in yticks])

    #plt.yticks([0, 5000000, 10000000, 15000000, 20000000, 25000000, 30000000, 35000000, 40000000, 45000000, 50000000], ['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M', '40M', '45M', '50M'])
    plt.ylabel('Distance (miles)')
    plt.grid(True)

    # Show the plot
    plt.show()