import numpy as np

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None
        self.headers = None

    def load_data(self):
        # Load headers
        self.headers = np.genfromtxt(
            self.filepath,
            delimiter=",",
            dtype=str,
            max_rows=1
        )

        # Load remaining data
        raw_data = np.genfromtxt(
            self.filepath,
            delimiter=",",
            dtype=str,
            skip_header=1
        )

        # Convert numeric columns to float (skip Name column)
        self.data = raw_data[:, 1:].astype(float)

        print("✅ Dataset Loaded Successfully!")
        return self.data
