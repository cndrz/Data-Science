import pandas as pd

energy_data = {

    "Timestamp": [
        "2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04", 
        "2026-01-05", "2026-01-06", "2026-01-07", "2026-01-08", 
        "2026-01-09", "2026-01-10", "2026-01-11", "2026-01-12", 
        "2026-01-13", "2026-01-14"
    ],

    "kWh_Used": [12, 15, 11, 14, 18, 20, 10, 13, 16, 11, 12, 19, 22, 15]
}

df = pd.DataFrame(energy_data)

df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df.set_index("Timestamp", inplace = True)
weekly_usage = df["kWh_Used"].resample("W").sum()

print("Weekly Energy Report: ")
print(weekly_usage)