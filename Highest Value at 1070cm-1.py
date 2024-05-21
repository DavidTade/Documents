# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:34:01 2024

@author: david
"""

import os

def find_highest_value_file(folder_path, target_value, column_index):
  """
  Searches for the file in the given folder with the highest value in the
  specified column, corresponding to the target value in another column.

  Args:
    folder_path (str): The path to the folder containing the txt files.
    target_value (float): The value to compare against in the specified column.
    column_index (int): The index of the column to check for the target value (0-based indexing).

  Returns:
    tuple: A tuple containing the path to the file with the highest value (or None if not found)
           and the highest value found.
  """

  highest_value_file = None
  highest_value = None

  for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
      file_path = os.path.join(folder_path, filename)
      try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
          for line in file:
            # Split the line based on tabs
            data = line.strip().split('\t')
            if len(data) > column_index:
              try:
                # Convert the target column value to float and compare
                if float(data[column_index]) == target_value:
                  value = float(data[column_index + 1])  # Second column value
                  if highest_value is None or value > highest_value:
                    highest_value = value
                    highest_value_file = file_path
              except ValueError:
                # Handle potential errors if the line cannot be converted to a float
                pass
      except FileNotFoundError:
        # Handle potential file not found errors
        pass

  return highest_value_file, highest_value

# Example usage (assuming you have permission to access the folder)
folder_path = "C:/Users/david/OneDrive - University of Birmingham/CDT/ANMSA/A-Year 4/Raman/May2024/16May/830nm-y-150deg"  # Replace with the actual folder path
target_value = 1070.758789
column_index = 0  # Assuming the target value is in the first column (0-based indexing)

highest_value_file, highest_value = find_highest_value_file(folder_path, target_value, column_index)

if highest_value_file:
  print("File with highest value:", highest_value_file)
  print("Highest value in second column:", highest_value)
else:
  print("No files found in the folder or no file has", target_value, "in the first column with a value in the second column.")
