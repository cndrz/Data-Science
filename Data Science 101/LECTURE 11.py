import pandas as pd

fitness_data = {

    "Athlete_ID": [101, 102, 103, 104, 105],
    "BPM": [50, 80, 65, 70, 90],
    "yrs_train": [1, 15, 5, 8, 2]
}

df = pd.DataFrame(fitness_data)
df["BPM_Normal"] = bpm_normal = (df["BPM"] - df["BPM"].min()) / (df["BPM"].max() - df["BPM"].min())
df ["Years_Normal"] = years_normal = (df["yrs_train"] - df["yrs_train"].min()) / (df["yrs_train"].max() - df["yrs_train"].min())
    
print("Normalized BPM and Years of Training: ")
print(bpm_normal)
print(years_normal)
