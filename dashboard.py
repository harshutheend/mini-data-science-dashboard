import numpy as np
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
        self.names = None
    def start(self):
        # Load data once
        self.data = self.loader.load_data()
        self.headers = self.loader.headers
        self.names = self.loader.names


        self.analyzer = DataAnalyzer(self.data, self.headers)
        self.visualizer = Visualizer(self.data, self.headers)

        while True:
            print("\n===== MINI DATA SCIENCE DASHBOARD =====")
            print("1. Show Summary Statistics")
            print("2. Show Correlation Matrix")
            print("3. Show Bar Chart")
            print("4. Show Histogram")
            print("5. Exit")
            print("6. Add New Record")
            print("7. Save Dataset")

            choice = input("Enter your choice: ")
            print("You entered:", choice)
            if choice == "1":
                self.analyzer.summary()
                input("\nPress Enter to continue...")
            elif choice == "2":
                self.analyzer.correlation()
                input("\nPress Enter to continue...")
            elif choice == "3":
                self.visualizer.bar_chart()
            elif choice == "4":
                self.visualizer.histogram()
            elif choice == "5":
                print("Exiting Dashboard...")
                break
            elif choice == "6":

                if self.data is None:
                    print(" Please load dataset first.")
                    continue

                try:
                    print("\nEnter new student details:")

                    name = input("Name: ")

                    new_marks = []

                    for subject in self.headers[1:]:
                        value = float(input(f"{subject}: "))
                        new_marks.append(value)

                    # Validate column count
                    if len(new_marks) != len(self.headers) - 1:
                        print(" Incorrect number of values.")
                        continue

                    # Append name
                    self.names = np.append(self.names, name)

                    # Append numeric row
                    new_row = np.array(new_marks)
                    self.data = np.vstack([self.data, new_row])

                    # Recreate analyzer & visualizer
                    self.analyzer = DataAnalyzer(self.data, self.headers)
                    self.visualizer = Visualizer(self.data, self.headers)

                    print(" Record Added Successfully!")

                except Exception as e:
                    print(" Invalid input:", e)
            elif choice == "7":

                if self.data is None:
                    print("⚠ N dataset loaded.")
                    continue

                try:
                    full_data = []

                    for i in range(len(self.names)):
                        row = [self.names[i]] + list(self.data[i])
                        full_data.append(row)

                    full_data = np.array(full_data)

                    # Add headers
                    final_data = np.vstack([self.headers, full_data])

                    np.savetxt(
                        self.loader.filepath,
                        final_data,
                        delimiter=",",
                        fmt="%s"
                    )

                    print(" Dataset Saved Successfully!")

                except Exception as e:
                    print(" Error saving file:", e)
            else:
                print("Invalid choice. Try again.")
