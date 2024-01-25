"""
Program: gui_template.py
Chapter 8
1/25/2024

**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

GUI-based version of the Salary Calculator app which calculates an employee's weekly earnings.
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports go here

# Class header (class name will change project to project)
class SalaryCalculator(EasyFrame):

    # Definition of our classes' constructor method
    def __init__(self):
        # Call to the Easy Frame class constructor
        EasyFrame.__init__(self, title = "Salary Calculator 2.0", width = 350, height = 400, background = "SkyBlue2")
        # variable to store a Font design for multiple labels
        labelFont = Font(family = "Lucida Sans", size = 14)

        # Add various components to the window
        self.addLabel(text = "Salary Calculator", row = 0, column = 0, sticky = "NSEW", columnspan = 2, background = "SkyBlue2", font = Font(family = "Gill Sans", size = 22))
        
        # Label and entry field for wage
        self.addLabel(text = "Hourly Wage", row = 1, column = 0, background = "SkyBlue2", foreground = "purple", font = labelFont)
        self.wageField = self.addFloatField(value = 0.0, row = 1, column = 1)

        # Label and entry field for hours worked
        self.addLabel(text = "No. of Hours Worked", row = 2, column = 0, background = "SkyBlue2", foreground = "purple", font = labelFont)
        self.hourField = self.addIntegerField(value = 0, row = 2, column = 1)
        # Bind the hourField to the press of the enter key event
        self.hourField.bind("<Return>", lambda event: self.compute())

        # Command button that computes salary
        self.button = self.addButton(text = "Calculate", row = 3, column = 0, columnspan = 2, command = self.compute)
        self.button["background"] = "green2"
        self.button["width"] = 15

        self.addLabel(text = "The emplyee's salary is: ", row = 4, column = 0, background = "SkyBlue2", font = labelFont)
        self.outputField = self.addFloatField(value = 0.0, row = 4, column = 1, precision = 2, state = "readonly")

    # Definition of the compute() function which is the event handler
    def compute(self):
        wage = self.wageField.getNumber()
        hours = self.hourField.getNumber()
        salary = wage * hours
        self.outputField.setNumber(salary)




# Global definition of the main() method
def main():
    # Instantiate an object from the class into mainloop()
    SalaryCalculator().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
    main()