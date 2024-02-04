"""
word_count.py

This scripts takes the .txt files in the P3 folder to identify all distintc words
and the frequencyy of each of them. The results are printed on a screen and on a 
filed named WordCountResults.txt. 

DENISSE MARIA RAMIREZ COLMENERO
A01561497
"""
import os
import time
import string

FOLDER = "P3"
EXTENSION = ".txt"
NEW_FILE_NAME = "WordCountResults.txt"

def count_frequency(file_path: str, new_file):
    """
    Count the frequencyy of each word in a file. 
    :param file_path: Path to the file
    :param new_file: File object to write the results
    """
    try:
        with open(file_path, 'r', encoding = 'utf-8') as file:
            new_file.write(f"\nWord frequency in file: {file_path}\n")

            frequency = {}

            for line in file:
                line = line.translate(str.maketrans("", "", string.punctuation)) # Remove puntuation
                words = line.lower().split() # Convert letters to lowercase only

                for word in words:
                    if word in frequency:
                        frequency[word] += 1 # Increment if word is already in the dictionary
                    else:
                        frequency[word] = 1 # Add the word to the dictionary

            # Create new sorted dictionary with each word and its frequency
            dic_word_frequency = dict(sorted(frequency.items(),
                                             key=lambda item: item[1], reverse=True))

            #Write the results in a new file
            for word, freq in dic_word_frequency.items():
                result = f"{word}: {freq}\n"
                print(result)
                new_file.write(result)

    except FileNotFoundError as e:
        print(f"File not found: {file_path} ({e})")
    except IOError as e:
        print(f"IOError: {e}")

def word_frequency_folder(folder_path: str):
    """
    Count the frequencyy of each word in all files in the folder. 
    :param folder_path: Path to the folder
    """
    with open(NEW_FILE_NAME, 'w', encoding='utf-8') as new_file:
        # List all files in the folder P3
        files = [f for f in os.listdir(folder_path) if f.endswith(EXTENSION)]

        # Word frequency in each file
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            count_frequency(file_path, new_file)

if __name__ == "__main__":
    start_time = time.time()

    try:
        if not os.path.isdir(FOLDER):
            raise FileNotFoundError(f"Invalid folder path: {FOLDER}")


        word_frequency_folder(FOLDER)

        print(f"\nResults written to {NEW_FILE_NAME}")

    finally:
        total_time = time.time() - start_time
        print(f"Total execution time: {total_time} seconds")
