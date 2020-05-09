# start of the build out of the options program
# starting super simple and calculating the current
# profitability of the option before any web scraping or anything like that

import pandas
import matplotlib
import numpy
import yfinance
import bs4 # for the web scraping on yahoo finance
import pprint
import pyinputplus as pyip
import os
import sys

# Calculating call option

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

option = pyip.inputMenu(['call','put','q'], numbered = True)

if option == 'call':
    print('Starting call option calculation.')
    callCalc()
elif option == 'put':
    print('Starting put option calculation.')
    putCalc()
elif option == 'q':
    print('Stopping execution of the program.')
    sys.exit()