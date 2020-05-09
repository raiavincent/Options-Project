# start of the build out of the options program
# starting super simple and calculating the current
# profitability of the option before any web scraping or anything like that

# UP TOP TO DO:
# Round all outputs to two decimal places.
# Add a global q for quit at any point in the program.
# DONE: Maybe add delays before each function starts just to make it look nicer.
# What may be nice is to generate a chart for profitability.


import pandas
import matplotlib
import numpy
import yfinance
import bs4 # for the web scraping on yahoo finance
import pprint
import pyinputplus as pyip
import os
import sys
import time

# Adding global variables up here.

execSleep = 1.5

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

# Calculating a married put, where the the investor has some downside insurance if the stock were to fall
# below the put price.Capital preserving strategy and limits the downside risk.

# I think this one needs to be worked on and understood more to properly write the code.
# THIS NEEDS TO BE WORKED ON BUT THE SKELETON IS THERE

def marriedPut():
    # Get the purchase price of the stock.
    purchasePrice = pyip.inputNum("Enter the price of the stock the investor paid: ")

    # Get the price paid for the put.
    putPrice = pyip.inputNum("Enter the price of the put the investor paid: ")

    # Strike price of the option.
    strikePrice = pyip.inputNum("Enter the strike price of the put: ")

    # Current price of the stock.
    stockPrice = pyip.inputNum("Enter the current price of the stock: ")

    # Current yield of the strategy.
    marriedPutYield = stockPrice - purchasePrice - putPrice

    print("The current yield of the strategy is: " + str(marriedPutYield))



option = pyip.inputMenu(['call','put','covered call','married put','q'], numbered = True)

if option == 'call':
    time.sleep(execSleep)
    print('Starting call option calculation.')
    callCalc()
elif option == 'put':
    time.sleep(execSleep)
    print('Starting put option calculation.')
    putCalc()
elif option == 'covered call':
    time.sleep(execSleep)
    print('Starting the calculation of a covered call.')
    coveredCall()
elif option == 'married put':
    time.sleep(execSleep)
    print('Starting the calculation of a married put.')
    marriedPut()
elif option == 'q':
    time.sleep(execSleep)
    print('Stopping execution of the program.')
    sys.exit()
