import json
import os


def save_to_file(data, filename):
    """
    Serialize data to a file in JSON format.
    :param data: The data to be serialized and saved.
    :param filename: The name of the file to write.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_from_file(filename):
    """
    Deserialize JSON data from a file.
    :param filename: The name of the file to read.
    :return: The deserialized data from the file.
    """
    if not os.path.exists(filename):  # Check if the file exists
        return None
    with open(filename, 'r') as file:
        return json.load(file)


def append_to_file(data, filename):
    """
    Append JSON data to a file, ensuring no data overwrites.
    :param data: A single data item to append to the file.
    :param filename: The name of the file to append data.
    """
    existing_data = load_from_file(filename)  # Load existing data
    if existing_data is None:
        existing_data = []  # Initialize as an empty list if the file is new
    existing_data.append(data)
    save_to_file(existing_data, filename)  # Re-save the entire list


def delete_file(filename):
    """
    Remove a file from the filesystem.
    :param filename: The name of the file to delete.
    """
    if os.path.exists(filename):
        os.remove(filename)  # Delete the file safely


def read_lines(filename):
    """
    Read all the lines of a text file.
    :param filename: The name of the file to read.
    :return: A list of strings, each representing a line in the file.
    """
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.readlines()
    return []
