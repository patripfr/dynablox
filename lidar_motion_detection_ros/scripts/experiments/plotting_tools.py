import csv
import numpy as np

def read_plot_data_csv(csv_file):
    """
    Read a single CSV file of a run (tsdf or ssc) and turn it into a dictionary.
    """
    data = {}
    with open(csv_file, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        for key in header:
            data[key] = []

        for row in reader:
            for i, r in enumerate(row):
                data[header[i]].append(float(r))
    return data

def verify_data(data, names, expected_num_entries=10):
    num_incomplete = 0
    for i, d in enumerate(data):
        if not "timestamp" in d:
            print(f"Warning: failed to read data for '{names[i]}'.")
            num_incomplete = num_incomplete + 1
            continue
        num_entries = len(d["timestamp"])
        if num_entries < expected_num_entries:
            print(
                f"Warning: Incomplete data for '{names[i]}' ({num_entries}/{expected_num_entries}).")
            num_incomplete = num_incomplete + 1
    num_samples = len(data)
    print(f"{num_samples-num_incomplete}/{num_samples} data entries are complete.")

def get_grid(data, field):
    if field not in data:
        print(f"Warning: Did not fiend field '{field}' to create grid from.")
        return np.array([np.nan])
    return np.array(data[field])


