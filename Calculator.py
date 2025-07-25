import csv
import time
import datetime
file_path = 'Calculations.csv'
def save_to_csv(data, file_path):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
def read_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
class Calculator:
    def __init__(self):
        self.result = 0
        try:
            with open(file_path, mode='x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Calculation Results"])
                writer.writerow(["Timestamp: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
                writer.writerow([])
        except FileExistsError:
            print("File already exists. Appending to existing file.")
        
    def add(self, *args):
        for arg in args:
            self.result += arg
        save_to_csv([["Result for addition: "], [self.result]], file_path)

    def subtract(self, *args):
        for arg in args:
            self.result -= arg
        save_to_csv([["Result for subtraction: "], [self.result]], file_path)

    def multiply(self, *args):
        if self.result == 0:
            self.result = 1
        for arg in args:
            self.result *= arg
        save_to_csv([["Result for multiplication: "], [self.result]], file_path)

    def divide(self, *args):
        for arg in args:
            if arg == 0:
                raise ValueError("Cannot divide by zero")
        for arg in args:
            self.result /= arg
        save_to_csv([["Result for division: "], [self.result]], file_path)
print("Calculator initialized. Ready for calculations.")
print('Previous results saved in Calculations.csv')
read_csv(file_path)
calculator = Calculator()
calculator.add(1, 5)
calculator.subtract(3,13)  
calculator.multiply(2,4,7)
calculator.divide(2)