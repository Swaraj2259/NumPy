import numpy as np

# Step 1: Take Input
days = int(input("Enter number of days: "))
aqi_values = []

print("Enter AQI values for each day (enter -1 for missing data):")
for i in range(days):
    val = float(input(f"Day {i+1} AQI: "))
    aqi_values.append(val)

aqi_array = np.array(aqi_values)

# Step 2: Clean missing values (-1 replaced with mean)
missing_mask = aqi_array == -1
mean_aqi = np.mean(aqi_array[~missing_mask])
aqi_array[missing_mask] = mean_aqi

print(f"\nCleaned AQI values: {aqi_array}")

# Step 3: Rolling Average (window of 3)
window = 3
weights = np.ones(window) / window
rolling_avg = np.convolve(aqi_array, weights, mode='valid')
print(f"\nRolling Average (last {window} days): {np.round(rolling_avg, 2)}")

# Step 4: Detect Spikes (threshold difference > 30)
spikes = np.where(np.abs(np.diff(aqi_array)) > 30)[0]
if len(spikes) == 0:
    print("\nNo significant pollution spikes detected.")
else:
    print("\nPollution spikes detected on days (next day shows the spike):")
    for spike_day in spikes:
        print(f"  Day {spike_day + 2} → AQI jumped from {aqi_array[spike_day]} to {aqi_array[spike_day + 1]}")