import csv

def calculate_sma(filename='orcl.csv', window=5):
    # Function to load data from CSV file into a list of dictionaries
    def load_data(filename):
        with open(filename, 'r') as file:
            return list(csv.DictReader(file))

    # Load data from the provided orcl.csv file
    data = load_data(filename)

    sma_values = []
    
    # Iterate through each day of the data starting from day 5
    for i in range(window - 1, len(data)):
        # Extract the closing prices of the last five days
        window_prices = [float(data[j]['Close']) for j in range(i - window + 1, i + 1)]
        
        # Calculate the Simple Moving Average (SMA) by averaging the prices
        sma = sum(window_prices) / window
        
        # Append date and calculated SMA to the list
        sma_values.append({'Date': data[i]['Date'], 'SMA': sma})

    return sma_values

# Example usage:
result = calculate_sma()
print(result)
