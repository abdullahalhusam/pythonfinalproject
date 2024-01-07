import csv

def calculate_rsi(filename='orcl.csv', periods=14):
    # Load data from the specified CSV file into a list of dictionaries
    def load_data(filename):
        with open(filename, 'r') as file:
            return list(csv.DictReader(file))

    # Load data from the provided orcl.csv file
    data = load_data(filename)
    
    # Initialize lists for gains, losses, and RSI values
    gains, losses, rsi_values = [], [], []

    # Iterate through each row of the data
    for i in range(1, len(data)):
        # Calculate the daily change in Close price
        change = float(data[i]['Close']) - float(data[i - 1]['Close'])
        
        # Append the change to gains if positive, otherwise append 0
        gains.append(max(change, 0))
        
        # Append the absolute value of change to losses if negative, otherwise append 0
        losses.append(abs(min(change, 0)))

        # Start calculating averages after the specified period (14 days)
        if i >= periods:
            # Calculate average gains and losses over the specified period
            avg_gain = sum(gains[-periods:]) / periods
            avg_loss = sum(losses[-periods:]) / periods

            # Calculate relative strength (rs) and RSI using the given formula
            rs = avg_gain / avg_loss if avg_loss != 0 else 0
            rsi = 100 - (100 / (1 + rs))

            # Append date and calculated RSI to the list
            rsi_values.append({'Date': data[i]['Date'], 'RSI': rsi})

    return rsi_values

# Example usage:
result = calculate_rsi()
print(result)
