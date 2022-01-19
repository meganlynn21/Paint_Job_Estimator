# Paint Job Estimator


import math

def main():
  # Get user input
  fWall_Sq_Feet = getFloatInput("Enter wall space in square feet: ")
  fPrice_PerGallon = getFloatInput("Enter paint price per gallon: ")
  fFeet_PerGallon = getFloatInput("Enter feet per gallon: ")
  fLabor_Hours_PerGallon = getFloatInput("How many labor hours per gallon: ")
  fLaborCharge = getFloatInput("Labor charge per hour: ")
  sState = str(input("State job is in: "))

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
  fState = getSalesTax(sState, fLaborCost, fPaintCost, iGetPaint)

# Cost estimate
  fCost = showCostEstimate(fLaborCost, fPaintCost, fState, iGetPaint, fLabor)
  fTotalCostFormatted = "{:,.2f}".format(fCost)
  print("Total cost: $", fTotalCostFormatted, sep = "")


# Get number of gallons of paint
# Returns a int and receives 2 floats
def getGallonsOfpaint(fTotalSquareFeet, fFeetPerGallon):
    iGallonsNeeded = math.ceil(fTotalSquareFeet/fFeetPerGallon)
    return iGallonsNeeded

# Returns the labor hours to paint the wall as a float
def getLaborHours(fLabor_Hours_PerGallon, iGallonsNeeded):
    return fLabor_Hours_PerGallon * iGallonsNeeded

# Returns the labor cost to paint the wall as a float
def getLaborCost(Labor_Hours_PerGallon, fLaborCharge):
    return Labor_Hours_PerGallon * fLaborCharge

# Returns the paint cost to paint the wall as a float
def getPaintCost(iGallonsNeeded, fPrice_PerGallon):
    return iGallonsNeeded * fPrice_PerGallon

# Takes in all the calculated values and outputs the values to the screen 
def showCostEstimate(fLaborCost, fPaintCost, fState, iGetPaint, fLabor):
    print("Gallons of paint: ", iGetPaint)
    print("Hours of labor: ", format(fLabor, ".1f")) 
    fPaintCostFormatted = "{:.2f}".format(fPaintCost)
    print("Paint charges: $", fPaintCostFormatted, sep = "")
    fTotalLaborCharges = fLaborCost * iGetPaint
    fTotalLaborChargesFormatted = "{:,.2f}".format(fTotalLaborCharges)
    print("Labor charges: $", fTotalLaborChargesFormatted, sep = "")
    fStateTaxFormatted = "{:.2f}".format(fState)
    print("Tax: $", fStateTaxFormatted, sep = "")
    return (fLaborCost * iGetPaint) + fPaintCost + fState

# Data validation
def getFloatInput(sPromptMessage):
    fInput = 0
    while fInput <= 0:
        try:
            fInput = float(input(sPromptMessage))
        except ValueError:
            print("Input must be a number.")
    return fInput

# Function that returns the tax rate for each state

def getSalesTax(sState, fLaborCost, fPaintCost, iGetPaint):
    fTaxRate = 0
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
    return (fLaborCost * iGetPaint + fPaintCost) * fTaxRate


main()   







