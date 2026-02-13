import numpy as np

class DataAnalyzer:
    def __init__(self, data, headers):
        self.data = data
        self.headers = headers[1:]  # Skip Name column

    def summary(self):
        print("\n SUMMARY STATISTICS\n")

        for i, subject in enumerate(self.headers):
            column = self.data[:, i]

            print(f"Subject: {subject}")
            print("Mean:", np.mean(column))
            print("Median:", np.median(column))
            print("Std Dev:", np.std(column))
            print("Max:", np.max(column))
            print("Min:", np.min(column))
            print("-" * 30)

    def correlation(self):
        print("\n📈 CORRELATION MATRIX\n")
        corr = np.corrcoef(self.data.T)
        print(corr)
