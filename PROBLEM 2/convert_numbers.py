"""
convert_numbers.py

This scripts takes the .txt files in the P2 folder and performs a convertion of each
numerical value in the file to binary and hexadecimal base. The results are displayed 
in a table and written to a new .txt file named ConvertionResults.txt. The time it took 
to execute the convertion is also printed. 

DENISSE MARIA RAMIREZ COLMENERO
A01561497
"""
import os
import time      # Obtain the time elapsed for the execution.

FOLDER = "P2"
EXTENSION = ".txt"
NEW_FILE_NAME = "ConvertionResults.txt"

def binary_base(n):
    """
    Convert each number in binary using two's complement
    for negative numbers
    """
    binario = []

    # Handle the sign
    sign = '-' if n < 0 else ''
    n = abs(n)

    # Convertion to binary
    while n > 0:
        binario.append(str(n % 2))
        n //= 2

    # Invert and add the sign
    binary_result = sign + ''.join(binario[::-1])

    return binary_result

def hexadecimal_base(n):
    """
    Convert each number in hexadecimal using two's complement
    for negative numbers
    """
    hexad = []

    sign = '-' if n < 0 else ''
    n = abs(n)

    while n > 0:
        remainder = n % 16
        hexad.append(str(remainder) if remainder < 10 else chr(ord('A') + remainder - 10))
        n //= 16

    hexa_result = sign + ''.join(hexad[::-1])

    return hexa_result

def convertions(file_path: str, error_list, new_file):
    """
    Convertion of the numbers in the files to binary and hexadecimal base.
    """
    try:
        with open(file_path, 'r', encoding = 'utf-8') as file:
            new_file.write(f"\nConverting numbers in file: {file_path}\n")
            for line in file:
                try:
                    num = int(line.strip())   # Convert a string into a int
                    number = f"Number: {num}"
                    binary = f"Binary: {binary_base(num)}"
                    hexadecimal = f"Hexadecimal: {hexadecimal_base(num)}"
                    results = f"{number:<15} {binary:<20} {hexadecimal}"
                    print(results)
                    new_file.write(results)

                except ValueError as ve:
                    error_list.append(f"Invalid data in {file_path}. \
                    Skipping line: {line.strip()}. Error: {ve}")

    except FileNotFoundError as e:
        print(f"File not found: {file_path} ({e})")
    except IOError as e:
        print(f"IOError: {e}")

def process_files_in_folder(folder_path: str) -> list:
    """
    Convertion of the numbers in all .txt files to binary and hexadecimal base.

    :param folder_path: Path to the folder
    """
    error_list = []
    with open(NEW_FILE_NAME, 'w', encoding='utf-8') as new_file:

        # List all files in the folder
        file_list = sorted([f for f in os.listdir(folder_path) if f.endswith(EXTENSION)])

        # Convert numbers in each file
        for file_name in file_list:
            file_path = os.path.join(folder_path, file_name)
            convertions(file_path, error_list, new_file)

    return error_list

if __name__ == "__main__":
    start_time = time.time()    # Record the start time
    try:
        if not os.path.isdir(FOLDER):    # Check if the specified folder path exists
            raise FileNotFoundError(f"Invalid folder path: {FOLDER}")

        errors = process_files_in_folder(FOLDER)
        print(f"\nResults written to {NEW_FILE_NAME}")

        if errors:
            print("\nEncountered ValueErrors:")
            for error in errors:
                print(error)
    finally:
        total_time = time.time() - start_time
        print(f"Total execution time: {total_time} seconds")
