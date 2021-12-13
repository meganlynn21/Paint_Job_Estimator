# Paint Job Estimator
# Megan Keyes
# A painting company has determined that for every 112 square feet of wall space,
# one gallon of paint and eight hours of labor will be required. The company
# charges $35 dollars per hour for labor. Write a program that asks the
# user to enter the square feet of wall space to be paonted and the price
# per gallon.

# stopped at 20:58


import math

#Need to get number of gallons of paint
#Return a int and receives 2 floats

def getGallonsOfpaint(TotalSquareFeetIn, FeetPerGallonIn):
    iGallonsNeeded = math.ceil(TotalSquareFeet/FeetPerGallon)
    return iGallonsNeeded

#

def getLaborHours(fLaborHoursPerGallonIn, fTotalGallonsIn):
    return fLaborHoursPerGallon * fTotalGallons

#Function for float input
def getFloatInput(sPromptMessage):
    fInput = 0
    while fInput <= 0:
        try:
            fInput = float(input(sPromptMessage))
        except ValueError:
            print("Input must be a number.")
    return fInput

def main():
    fWall_Sq_Feet = getFloatInput("Enter wall space in square feet: ")
    fPrice_PerGallon = getFloatInput("Enter paint price per gallon: ")
    fFeet_PerGallon = getFloatInput("Enter feet per gallon: ")
    fLabor_Hours_PerGallon = getFloatInput("How many labor hours per gallon: ")
    fLaborCharge = getFloatInput("Labor charge per hour: ")
    








main()


    







