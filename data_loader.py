import numpy as np

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None
        self.headers = None
        self.names = None

    def load_data(self):

        raw_data = np.genfromtxt(
            self.filepath,
            delimiter=",",
            dtype=str,
            skip_header=1
        )

        self.headers = np.genfromtxt(
            self.filepath,
            delimiter=",",
            dtype=str,
            max_rows=1
        )

        # Separate names and numeric data
        self.names = raw_data[:, 0]
        self.data = raw_data[:, 1:].astype(float)

        print(" Dataset Loaded Successfully!")
        return self.data
