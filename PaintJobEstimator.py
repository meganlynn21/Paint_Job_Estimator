# Paint Job Estimator
# Megan Keyes
# A painting company has determined that for every 112 square feet of wall space,
# one gallon of paint and eight hours of labor will be required. The company
# charges $35 dollars per hour for labor. Write a program that asks the
# user to enter the square feet of wall space to be painted and the price
# per gallon.

import math

def main():
    # Get user input
  fWall_Sq_Feet = getFloatInput("Enter wall space in square feet: ")
  fPrice_PerGallon = getFloatInput("Enter paint price per gallon: ")
  fFeet_PerGallon = getFloatInput("Enter feet per gallon: ")
  fLabor_Hours_PerGallon = getFloatInput("How many labor hours per gallon: ")
  fLaborCharge = getFloatInput("Labor charge per hour: ")
  sState = str(input("State job is in: "))
  sLastName = str(input("Customer Last Name: "))

# Call Functions

# Get paint int
  iGetPaint = getGallonsOfpaint(fWall_Sq_Feet, fFeet_PerGallon)

# Labor hours
  fLabor = getLaborHours(fLabor_Hours_PerGallon, iGetPaint)

# Labor cost
  fLaborCost = getLaborCost(fLabor_Hours_PerGallon, fLaborCharge)

# Paint cost
  fPaintCost = getPaintCost(iGetPaint, fPrice_PerGallon)

# State Tax
  fState = getSalesTax(sState)

# Cost estimate
  fCost = showCostEstimate(fLaborCost, fPaintCost, fState)

# Need to get number of gallons of paint
# Return a int and receives 2 floats
def getGallonsOfpaint(fTotalSquareFeet, fFeetPerGallon):
    iGallonsNeeded = math.ceil(fTotalSquareFeet/fFeetPerGallon)
    return iGallonsNeeded

# Returns the labor hours to paint the wall as a float
def getLaborHours(fLaborHoursPerGallon, fTotalGallons):
    return fLaborHoursPerGallon * fTotalGallons

# Returns the labor cost to paint the wall as a float
def getLaborCost(LaborHoursPerGallon, fLaborCharge):
    return LaborHoursPerGallon * fLaborCharge

# Returns the paint cost to paint the wall as a float
def getPaintCost(iGallonsNeeded, fPaintCost):
    return iGallonsNeeded * fPaintCost

# Show cost estimate function
def showCostEstimate(fLaborCost, fPaintCost, fState):
    print("Gallons of paint: ", iGetPaint)
    print("Hours of labor: ", format(fLabor, ".1f"))
    print("Paint charges: ", format(fPaintCost, ".2f"))
    print("Labor charges: ", format(fLaborCost, ".2f"))
    print("Tax: ", format(fState, ".2f"))
    print("Total cost: ", format(fCost, ".2f"))
    return fLaborCost + fPaintCost * fState

# Function for float input
def getFloatInput(sPromptMessage):
    fInput = 0
    while fInput <= 0:
        try:
            fInput = float(input(sPromptMessage))
        except ValueError:
            print("Input must be a number.")
    return fInput

# State function

def getSalesTax(sState):
    if sState == "CT":
         fTaxRate = .06
    elif sState == "MA":
         fTaxRate = .0625
    elif sState == "ME":
         fTaxRate = .085
    elif sState == "NH":
         fTaxRate = .0
    elif sState == "RI":
         fTaxRate = .07
    elif sState == "VT":
         fTaxRate = .06
    else:
        print("Not a valid input")

    return fTaxRate


main()   







