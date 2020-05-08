# start of the build out of the options program
# starting super simple and calculating the current profitability of the option

import pandas
import matplotlib
import numpy
import yfinance
import bs4 # for the web scraping on yahoo finance
import pprint
import pyinputplus as pyip

# Start by getting the current price of the option.

optionPrice = pyip.inputNum("Enter the current price of the option contract: ")

# Next we will get the price of the stock.

stockPrice = pyip.inputNum("Enter the current price of the stock: ")

# Maybe I also need the strike price of the option

strikePrice = pyip.inputNum("Enter the strike price associated with the contract: ")

# Probably also need the premium!

premium = pyip.inputNum("Enter the premium associated with the option: ")
