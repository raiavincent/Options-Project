# start of the build out of the options program
# starting super simple and calculating the current
# profitability of the option before any web scraping or anything like that

# UP TOP TO DO:
# TODO Round all outputs to two decimal places.
# TODO Add a global q for quit at any point in the program.
# DONE Maybe add delays before each function starts just to make it look nicer.
# TODO Generate a chart for profitability.
# TODO Add descriptions of each strategy at the start.
# Done Add straddles.
# TODO Add strangles.
# TODO Add iron condors.
# TODO Add butterfly spreads.


import pandas
import matplotlib
import numpy
import yfinance
import bs4  # for the web scraping on yahoo finance
import pprint
import pyinputplus as pyip
import os
import sys
import time

# Adding global variables up here.

execSleep = 1.5  # Before starting execution of the function to calculate.
definitionSleep = 3  # Giving user time to read the definition.
startSleep = 1  # Print the option chosen and then starting with a slight delay.


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

    print("The current intrinsic value is " + str(intrinsicValue) + ".")

    # Calculating the time value of the option

    timeValue = optionPrice - intrinsicValue

    print("The current time value is " + str(timeValue) + ".")


# Calculations on put option.

def putCalc():
    optionPrice = pyip.inputNum("Enter the current price of the option contract: ")

    # Next we will get the price of the stock.

    stockPrice = pyip.inputNum("Enter the current price of the stock: ")

    # Maybe I also need the strike price of the option.

    strikePrice = pyip.inputNum("Enter the strike price associated with the contract: ")

    # Calculating the intrinsic value of the option.

    intrinsicValue = strikePrice - stockPrice

    print("The current intrinsic value is " + str(intrinsicValue) + ".")

    # Calculating the time value of the option

    timeValue = optionPrice - intrinsicValue

    print("The current time value is " + str(timeValue) + ".")


# Calculating a covered call, which is where an investor may like the stock, but to cover some downside risk in the mean
# time, will sell a call option to generate income on the premiums.

def coveredCall():
    # Stock price first, this is what the investor bought the stock at.

    purchasePrice = pyip.inputNum("Enter the price of the stock the investor paid: ")

    # Then we need the premium received for selling the call.

    premium = pyip.inputNum("Enter the premium the investor gained by selling the call: ")

    # Current price of the stock to determine the investor's position.

    stockPrice = pyip.inputNum("Enter the current price of the stock to determine the investor's yield: ")

    # And determine the yield currently as of now.

    coveredYield = premium + stockPrice - purchasePrice
    print('The investors current yield is ' + str(coveredYield) + '.')


# Calculating a married put, where the the investor has some downside insurance if the stock were to fall
# below the put price.Capital preserving strategy and limits the downside risk.

# I think this one needs to be worked on and understood more to properly write the code.
# THIS NEEDS TO BE WORKED ON BUT THE SKELETON IS THERE
# Maybe not even include this? Keep it for now.

def marriedPut():
    # Get the purchase price of the stock.
    purchasePrice = pyip.inputNum("Enter the price of the stock the investor paid: ")

    # Get the price paid for the put.
    putPrice = pyip.inputNum("Enter the price of the put the investor paid: ")

    # Strike price of the option.
    strikePrice = pyip.inputNum("Enter the strike price of the put: ")

    # Current price of the stock.
    stockPrice = pyip.inputNum("Enter the current price of the stock: ")

    netDebit = stockPrice + putPrice
    breakEven = netDebit
    maximumRisk = netDebit - strikePrice
    percentMaxRisk = maximumRisk / netDebit

    percentageRisk = "{:.2%}".format(percentMaxRisk)

    print('Outlay: ' + str(netDebit))
    print('(This is also the break even point.)')
    print('Maximum Risk: ' + str(maximumRisk))
    print('Investor is risking ' + str(percentageRisk) + ' of the outlay.')
    print('The investor has a maximum profit that is unlimited.')


# Spreads, start with credit.
# TODO Simulation as to changes in the strike prices and the profit change.

def creditSpread():
    # First need the price of the high premium option to be sold.
    highPrem = pyip.inputNum("Enter the price of the high-premium option to be sold: ")

    # Next the price of the lower premium option to be bought.
    lowPrem = pyip.inputNum("Enter the price of the low-premium option to be bought: ")

    # Current profit of the spread.
    netPremium = highPrem - lowPrem

    # And print it.
    print("The investor has a net premium of " + str(netPremium) + ".")


def debitSpread():
    # First need the price of the high premium option to be sold.
    highPrem = pyip.inputNum("Enter the price of the high-premium option to be bought: ")

    # Next the price of the lower premium option to be bought.
    lowPrem = pyip.inputNum("Enter the price of the low-premium option to be sold: ")

    # Current profit of the spread.
    netPremium = lowPrem - highPrem

    # And print it.
    print("The investor has netted $" + str(netPremium) + " on the trade currently.")

def straddle():
    # Price of the put option.
    putPrice = pyip.inputNum('Enter the premium paid for the put option:')

    # Price of the call option.
    callPrice = pyip.inputNum('Enter the price of the call option:')

    # Strike price.
    strikePrice = pyip.inputNum('Enter the strike price of both options: ')

    premTotal = putPrice + callPrice
    print('The price to put together the straddle is $' + premTotal ', not considering the price of the stock.')

    # Get the cost of the stock.
    pricePaid = pyip.inputNum('Enter the price paid for the stock: ')

    # Determine the break even point.
    breakEvenRise = pricePaid + premTotal
    breakEvenFall = pricePaid - premTotal
    print('The investor breaks even at $' + breakEvenRise + ' and '+ breakEvenFall + '.')

    # Calculate the current profit or loss.
    # Get the stock's current price.
    stockPrice = pyip.inputNum('Enter the current price of the stock: ')

    # TODO Test calculation of position of a straddle.

    # Current position.
    position1 = stockPrice - breakEvenRise
    position2 = stockPrice - breakEvenFall

    if position1 > position2:
        print("The investor currently has a position of $" + position1 + " with the strategy.")
    else:
        print("The investor currently has a position of $" + position2 + " with the strategy.")


option = pyip.inputMenu(['call', 'put', 'covered call', 'married put', 'credit spread', 'debit spread', 'straddle', 'q'],
                        numbered=True)

if option == 'call':
    print('Call option selected.')
    time.sleep(startSleep)
    print('A call option gives an investor the right, but not the obligation, to buy a stock at a certain price, '
          'the strike price.')
    time.sleep(definitionSleep)
    print('Starting call option calculation.')
    time.sleep(execSleep)
    callCalc()
elif option == 'put':
    print('Put option selected.')
    time.sleep(startSleep)
    print('A put option gives an investor the right, but not the obligation, to sell a stock at a certain price, '
          'the strike price.')
    time.sleep(execSleep)
    print('Starting put option calculation.')
    putCalc()
elif option == 'covered call':
    print('Covered call strategy selected.')
    time.sleep(startSleep)
    print('A covered call is a transaction where an investor sells a call option and owns the equivalent amount of '
          'the underlying security. To execute, the investor is long the asset then sells calls on the same asset to '
          'generate income. This is a neutral strategy, meaning the investor only expects a minor increase in the '
          'underlying stock price of the written call opttion. Usually employed if an investor wants to hold the '
          'stock for a long time but does not expect near term appreciation, so generates income from the option '
          'premium.')
    time.sleep(execSleep)
    print('Starting the calculation of a covered call.')
    coveredCall()
elif option == 'married put':
    print('Married put strategy selected.')
    time.sleep(startSleep)
    print('A married put is a strategy where an investor is long the asset and purchases an at the money put option '
          'on the same asset to protect against depreciation of said asset. The investor essentially protects against '
          'the downside risk yet can still participate in any gains from the upside. ')
    time.sleep(execSleep)
    print('Starting the calculation of a married put.')
    marriedPut()
elif option == 'credit spread':
    print('Credit spread selected.')
    time.sleep(startSleep)
    print('A credit spread involves the sale of a high premium option followed by the purchase of a lower premium '
          'option. Premium received from writing is greater than purchasing, resulting in a premium. This is the '
          'maximum profit.')
    time.sleep(execSleep)
    print('Starting the credit spread calculation.')
    creditSpread()
elif option == 'debit spread':
    print('Debit spread selected.')
    time.sleep(startSleep)
    print('A debit spread involves buying a high premium option and then selling an option at a lower premium. This '
          'results in a premium paid by the investor. Used to offset the costs associated with owning long options '
          'positions.')
    time.sleep(execSleep)
    print('Starting the debit spread calculation.')
    debitSpread()
elif option == 'straddle':
    print('Straddle selected.')
    time.sleep(startSleep)
    print('A straddle involves the purchase of a put and a call at the same strike price and expiration date. Profit '
          'occurs when the stock rices or falls more than the premium paid on the strategy. Profit potential is '
          'unlimited.')
    time.sleep(execSleep)
    print('Starting the straddle calculation.')
    straddle()
elif option == 'q':
    time.sleep(execSleep)
    print('lol q is not a strategy, you just stopped the program.')
    sys.exit()
