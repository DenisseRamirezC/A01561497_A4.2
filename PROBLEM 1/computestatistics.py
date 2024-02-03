"""
computestatistics.py

This scripts takes the .txt files in the P1 folder and performs statistical operations 
with the list of numerical values of each file and gets the time it took to execute the 
operations. The results are displayed in a table and written to a new .txt file called
StatisticsResults.txt

DENISSE MARIA RAMIREZ COLMENERO
A01561497
"""
import os
import math
import time      # Obtain the time elapsed for the execution and calculations.
from tabulate import tabulate

FOLDER = "P1"
EXTENSION = ".txt"
NEW_FILE_NAME = "StatisticsResults.txt"

def calculate_statistics(file_path: str) -> list:
    """
    Creates a list with the values of each file and uses it to perform the operations.
    :param file_path: Path to the file
    :return: results of the operations ["Count", "Non-Zero Count", "Mean", "Median",
                              "Mode", "Variance", "Standard Deviation"]
    """
    try:
        start_time = time.time() # Record the start time
        with open(file_path, 'r', encoding = 'utf-8') as file:
            data = []
            for line in file:
                try:
                    # Converts each line into a float number and add it to the list data
                    data.append(float(line.strip()))
                except ValueError:
                    print(f"Invalid data in {file_path}. Skipping line: {line.strip()}")

            if not data:
                print(f"The {file_path} does not contain valid numerical data")
                return []

            count = len(data) # Calculate statistics
            mean = round(sum(data) / count, 2)
            sorted_list = sorted(data)
            median = sorted_list[count // 2] if count % 2 == 1 else (sorted_list[count // 2 - 1]
                                                                 + sorted_list[count // 2]) / 2

            mode = max(set(data), key=data.count)

            standard_deviation = round(math.sqrt(sum((x - mean) ** 2 for x in data) / count), 2)
            variance = round(sum((x - mean) ** 2 for x in data) / count,2)


            end_time = time.time() # Record the end time
            elapsed_time = round(end_time - start_time,2) # Calculate the elapsed time

            return [count, count - data.count(0), mean, median,
                    mode, variance, standard_deviation, elapsed_time]


    except FileNotFoundError as e:
        print(f"File not found: {file_path} ({e})")
    except IOError as e:
        print(f"IOError: {e}")
    return []

def process_files_in_folder(folder_path: str) :
    """
    Process each file in a folder and display statistics.
    :param folder_path: Path to the folder
    """
    results_table = []
    # Create list of all files in the folder with the .txt extension
    file_list = sorted([f for f in os.listdir(folder_path) if f.endswith(EXTENSION)])

    # Process each file
    for file_name in file_list:
        # Constructs the full path to the current file
        file_path = os.path.join(folder_path, file_name)
        results = calculate_statistics(file_path)
        if results:
            # Add a new line to the table
            results_table.append([file_name] + results)

    return results_table

def display_table(results_table: list) -> None:
    """
    Display the calculation results in a table 

    """
    headers = ["File", "Count", "Non-Zero Count", "Mean", "Median",
               "Mode", "Variance", "Standard Deviation", "Elapsed Time"]
    print(tabulate(results_table, headers=headers, tablefmt="pretty"))

def statistics_results_file(results_table: list, total_time: float) -> None:
    """
    Write the statistical results in a table in a new file 
    """
    # Write the resulted statistics to a new file
    with open(NEW_FILE_NAME, 'w', encoding='utf-8') as output_file:
        headers = ["File"] + ["Count", "Non-Zero Count", "Mean", "Median",
                              "Mode", "Variance", "Standard Deviation", "Elapsed Time"]
        total_time_row = ["Total Time", total_time]
        results_table.append(total_time_row)
        output_file.write(tabulate(results_table, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    if not os.path.isdir(FOLDER): # Check if the specified folder path exists
        print("Invalid folder path")
    else:
        total_start_time = time.time()
        results_table_doc = process_files_in_folder(FOLDER)
        total_end_time = time.time()

        if results_table_doc:
            total_time_ = total_end_time - total_start_time
            display_table(results_table_doc)
            statistics_results_file(results_table_doc, total_time_ )
            print(f"Results written to {NEW_FILE_NAME}")
            print('Total time: ', total_time_)
