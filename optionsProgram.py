# start of the build out of the options program
# starting super simple and calculating the current
# profitability of the option before any web scraping or anything like that

# UP TOP TO DO:
# Round all outputs to two decimal places.


import pandas
import matplotlib
import numpy
import yfinance
import bs4 # for the web scraping on yahoo finance
import pprint
import pyinputplus as pyip
import os
import sys

# Calculations on call option,

# Start defining the calculations.

def callCalc():
    optionPrice = pyip.inputNum("Enter the current price of the option contract: ")

    # Next we will get the price of the stock.

    stockPrice = pyip.inputNum("Enter the current price of the stock: ")

    # Maybe I also need the strike price of the option.

    strikePrice = pyip.inputNum("Enter the strike price associated with the contract: ")

    # Calculating the intrinsic value of the option.

    intrinsicValue = stockPrice - strikePrice

    print("The current intrinsic value is " + str(intrinsicValue))

    # Calculating the time value of the option

    timeValue = optionPrice - intrinsicValue

    print("The current time value is " + str(timeValue))

# Calculations on put option.

def putCalc():
    optionPrice = pyip.inputNum("Enter the current price of the option contract: ")

    # Next we will get the price of the stock.

    stockPrice = pyip.inputNum("Enter the current price of the stock: ")

    # Maybe I also need the strike price of the option.

    strikePrice = pyip.inputNum("Enter the strike price associated with the contract: ")

    # Calculating the intrinsic value of the option.

    intrinsicValue = strikePrice - stockPrice

    print("The current intrinsic value is " + str(intrinsicValue))

    # Calculating the time value of the option

    timeValue = optionPrice - intrinsicValue

    print("The current time value is " + str(timeValue))

# Calculating a covered call, which is where an investor may like the stock, but to cover some downside risk in the mean
# time, will sell a call option to generate income on the premiums.

def coveredCall():

    # Stock price first, this is what the investor bought the stock at.

    purchasePrice = pyip.inputNum("Enter the price of the stock the investor paid: ")

    # Then we need the premium received for selling the call.

    premium = pyip.inputNum("Enter the premium the investor gained by selling the call: ")

    # Current price of the stock to determine the investor's position.

    stockPrice = pyip.inputNum("Enter the current price of the stock to determine the investor's yield: ")

    # And determin the yield currently as of now.

    coveredYield = premium + stockPrice - purchasePrice
    print('The investors current yield is ' + str(coveredYield))

option = pyip.inputMenu(['call','put','covered call','q'], numbered = True)

if option == 'call':
    print('Starting call option calculation.')
    callCalc()
elif option == 'put':
    print('Starting put option calculation.')
    putCalc()
elif option == 'covered call':
    print('Starting the calculation of a covered call.')
    coveredCall()
elif option == 'q':
    print('Stopping execution of the program.')
    sys.exit()
