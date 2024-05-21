# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:01:31 2024

@author: david
"""

import os

# Define the path to the directory containing the txt files
dir_path = "C:/Users/david/OneDrive - University of Birmingham/CDT/ANMSA/A-Year 4/Raman/May2024/16May/785nm-y-150deg"
target_wavenumber = 1070.082031

# Dictionary to store the values and filenames
values_dict = {}

# Loop over all files in the directory
for filename in os.listdir(dir_path):
    # Check if the file has the txt extension
    if filename.endswith(".txt"):
        # Open the file and read the data
        with open(os.path.join(dir_path, filename), "r") as f:
            for line in f:
                wavenumber, intensity = line.split("\t")
                if float(wavenumber) == target_wavenumber:
                    values_dict[filename] = float(intensity)
                    break

# Sort the dictionary by values
sorted_values = sorted(values_dict.items(), key=lambda item: item[1], reverse=True)

# Get the required files and values
highest_file, highest_value = sorted_values[0]
second_highest_file, second_highest_value = sorted_values[1]
third_highest_file, third_highest_value = sorted_values[2]
lowest_file, lowest_value = sorted_values[-1]

# Print the results
print(f"The file with the highest value is {highest_file} with a value of {highest_value}.")
print(f"The file with the second highest value is {second_highest_file} with a value of {second_highest_value}.")
print(f"The file with the third highest value is {third_highest_file} with a value of {third_highest_value}.")
print(f"The file with the lowest value is {lowest_file} with a value of {lowest_value}.")
