from data_loader import DataLoader
from analyzer import DataAnalyzer
from visualizer import Visualizer

class Dashboard:
    def __init__(self):
        self.loader = DataLoader("data/students.csv")
        self.data = None
        self.headers = None
        self.analyzer = None
        self.visualizer = None

    def start(self):
        # Load data once
        self.data = self.loader.load_data()
        self.headers = self.loader.headers

        self.analyzer = DataAnalyzer(self.data, self.headers)
        self.visualizer = Visualizer(self.data, self.headers)

        while True:
            print("\n===== MINI DATA SCIENCE DASHBOARD =====")
            print("1. Show Summary Statistics")
            print("2. Show Correlation Matrix")
            print("3. Show Bar Chart")
            print("4. Show Histogram")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.analyzer.summary()
            elif choice == "2":
                self.analyzer.correlation()
            elif choice == "3":
                self.visualizer.bar_chart()
            elif choice == "4":
                self.visualizer.histogram()
            elif choice == "5":
                print("Exiting Dashboard...")
                break
            else:
                print("Invalid choice. Try again.")
