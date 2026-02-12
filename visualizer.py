import matplotlib.pyplot as plt
import numpy as np

class Visualizer:
    def __init__(self, data, headers):
        self.data = data
        self.headers = headers[1:]  # Skip Name column

    def bar_chart(self):
        means = np.mean(self.data, axis=0)

        plt.figure()
        plt.bar(self.headers, means)
        plt.title("Average Marks per Subject")
        plt.xlabel("Subjects")
        plt.ylabel("Average Marks")
        plt.show()

    def histogram(self):
        plt.figure()
        plt.hist(self.data, bins=5)
        plt.title("Marks Distribution")
        plt.xlabel("Marks")
        plt.ylabel("Frequency")
        plt.show()
