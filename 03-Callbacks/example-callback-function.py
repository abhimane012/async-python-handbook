# Callback function example in Python

def fetch_data(callback):
    print("Fetching data...")
    
    # Simulating data fetched
    data = {"name": "Abhishek", "age": 25}
    
    # calling callback function with data
    callback(data)

def process_data(data):
    print("Processing data:")
    print(data)

fetch_data(process_data)