import pandas as pd

weather_data = {

    "City" : ["Caloocan","Quezon","Cebu","Davao","Manila",],
    "Temperature (Celsius)" : [30, 35, 32, 21, 18]
}

df = pd.DataFrame(weather_data)

df["Temperature (Fahrenheit)"] = (df["Temperature (Celsius)"] * 9/5) + 32

print(df)