# imports
import pandas as pd
import matplotlib.pyplot as plt

# 2) load the dataset
pd.options.display.max_columns = None
pd.options.display.max_rows = None

mydf = pd.read_csv('rideshare.csv')
print("2) Print the dataframe and find any nulls **********")
print(mydf)
print("\nAny Nulls?:", mydf.info())

# 3) Best Predictor of Distance

print("\n\n3) Find the best Predictor of Distance **********")
print("\nHour vs Distance", mydf['hour'].corr(mydf.distance))
print("Day vs Distance", mydf['day'].corr(mydf.distance))
print("Month vs Distance", mydf['month'].corr(mydf.distance))
print("Temperature vs Distance", mydf['temperature'].corr(mydf.distance))
print("Precipitation Probability vs Distance", mydf['precipProbability'].corr(mydf.distance))
print("Humidity vs Distance", mydf['humidity'].corr(mydf.distance))
print("Wind Speed vs Distance", mydf['windSpeed'].corr(mydf.distance))
print("Wind Gust vs Distance", mydf['windGust'].corr(mydf.distance))
print("Dew Point vs Distance", mydf['dewPoint'].corr(mydf.distance))
print("Pressure vs Distance", mydf['pressure'].corr(mydf.distance))
print("Cloud Cover vs Distance", mydf['cloudCover'].corr(mydf.distance))
print("Ozone vs Distance", mydf['ozone'].corr(mydf.distance))
print("Moon Phase vs Distance", mydf['moonPhase'].corr(mydf.distance))
# After looking through the different correlation coefficents cloud cover
# has the highest absolute value, so it is the best predictor of distance, even
# though it's value is only .75, which isn't great.

# 4) Scatter Plot of Cloud Cover vs Distance

plt.scatter(mydf.cloudCover, mydf.distance)
plt.xlabel("Cloud Cover")
plt.ylabel("Distance")
plt.show()
