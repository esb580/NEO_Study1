# Pull data series from NASA APIs selecting distance in miles and dates of NEO ID 3542519.
# URL https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=DEMO_KEY
from neo_lib import get_neo_data, visualize_neo_data, clean_neo_data

api_key = "DEMO_KEY"
neo_id = "3542519"
df = get_neo_data(neo_id, api_key)

# Clean the data
df = clean_neo_data(df)

# Print the DataFrame
print(df)

# Visualize the data
visualize_neo_data(df)



