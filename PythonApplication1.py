import csv

# Task 1
def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

file_path = 'orcl.csv'
historical_data = load_data(file_path)

# Print the first few rows of the loaded data for verification
for i in range(min(5, len(historical_data))):
    print(historical_data[i])

# Space to make it look neat and cool iykyk
print(" ")
print("----------------")
print(" ")

# Task 2 c2ti= Calculate two technical indicators - sma5= simple Moving Averagesfor a 5-day window - rsi14= Relative Strength Index (RSI)for a 14-day window
def c2ti(data):
    sma5 = []
    rsi14 = []

    for i in range(len(data)):
        # i) Simple Moving Averagesfor a 5-day window
        if i >= 4:
            close_prices_5 = [float(data[j]['Close']) for j in range(i-4, i+1)]
            sma5.append(sum(close_prices_5) / 5)

        # ii) Relative Strength Index (RSI)for a 14-day window
        if i >= 13:
            gains = losses = 0
            for j in range(i-13, i):
                price_change = float(data[j+1]['Close']) - float(data[j]['Close'])
                if price_change > 0:
                    gains += price_change
                else:
                    losses += abs(price_change)

            avg_gain = (gains / 14) if gains else 0
            avg_loss = (losses / 14) if losses else 0

            if avg_loss == 0:
                rsi14.append(100)
            else:
                relative_strength = avg_gain / avg_loss
                rsi = 100 - (100 / (1 + relative_strength))
                rsi14.append(rsi)

    return sma5, rsi14

# Task 3: Write indicators to separate CSV files
def write_to_csv(file_path, header, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)


# Calculate indicators
sma5, rsi14 = c2ti(historical_data)

# Print SMA & RSI
print("SMA for the first 5 days:", sma5[:5])
print("RSI for the first 14 days:", rsi14[:14])

