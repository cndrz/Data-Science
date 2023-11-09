import pandas as pd
import numpy as np

data_frame = pd.DataFrame({"X":[10, 20, 30, 40, 50], "Y":[2, 4, 6, 8, 10], "Z":[1, 2, 3, 4, 5]})

print("first n rows of the data frame")
data_frame_first_rows = data_frame.head(2) # first n rows of the data frame.
print(data_frame_first_rows) # prints the first rows specified.
print()

print("last n rows of the data frame")
data_frame_last_rows = data_frame.tail(3) # last n rows of the data frame.
print(data_frame_last_rows) # prints the first rows specified.
print()

print("numbers of rows and columns of the data frame")
data_frame_shape = data_frame.shape # number of rows and columns of the data frame.
print(data_frame_shape) # prints the value of rows and columns of the data frame.
print()

print("additional information about the data frame")
data_frame_information = data_frame.info() # index, datatype and memory information of the data frame.
print(data_frame_information) # prints the information mentioned about the data frame.
print()

print("statistics summary of the data frame")
data_frame_stat_summary = data_frame.describe() #  statistics summary of the data frame.
print(data_frame_stat_summary) # prints the summary statistics of the data frame.
print()



