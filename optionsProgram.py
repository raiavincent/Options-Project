# start of the build out of the options program
# starting super simple and calculating the current
# profitability of the option before any web scraping or anything like that

# UP TOP TO DO:
# Done Round all outputs to two decimal places.
# TODO Add a global q for quit at any point in the program.
# DONE Maybe add delays before each function starts just to make it look nicer.
# TODO Generate a chart for profitability.
# DONE Add descriptions of each strategy at the start.
# DONE Add straddles.
# DONE Add strangles.
# DONE Add iron condors.
# TODO Add butterfly spreads.
# DONE Add new lines in the explanations.
# DONE Implement yFinance to pull the current price of the stock.
# TODO Change the prompts.
# Dissect this for prompting:
# bT = pyip.inputMenu(['a','b'],
#  ...:   ...: prompt = 'What type of bread would you like ?\n* %s \n* %s \n* %s \n')

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

# ||||MARRIED PUT IS FINE NOW DISREGARD|||| as of 5/16/2020
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


# Straddle, buying call and put at same date and exercise, profit on down or up swings.
# Done Determine necessary percentage swing.
def straddle():
    # Price of the put option.
    putPrice = pyip.inputNum('Enter the premium paid for the put option: ')

    # Price of the call option.
    callPrice = pyip.inputNum('Enter the price of the call option: ')

    # Strike price.
    strikePrice = pyip.inputNum('Enter the strike price of both options: ')

    premTotal = putPrice + callPrice
    print('The price to put together the straddle is $' + str(premTotal) + ', not considering the price of the stock.')

    # Necessary swing.
    swing = premTotal / strikePrice
    swing = "{:.2%}".format(swing)
    print('To make a profit, the investor would need a swing of ' + swing + ' in the price of the asset.')

    # Get the cost of the stock.
    pricePaid = pyip.inputNum('Enter the price paid for the stock: ')

    # Determine the break even point.
    breakEvenRise = pricePaid + premTotal
    breakEvenFall = pricePaid - premTotal
    print('The investor breaks even at $' + str(breakEvenRise) + ' and $' + str(breakEvenFall) + '.')

    # Calculate the current profit or loss.
    # Get the stock's current price.
    stockPrice = pyip.inputNum('Enter the current price of the stock: ')

    # DONE Test calculation of position of a straddle.
    # DONE Calculate, for straddle put and call position separately, and then combine them, but either cannot be neg.

    # Current positions of each option.
    callPosition = stockPrice - strikePrice
    putPosition = strikePrice - stockPrice

    # Calculate total
    if callPosition < 0 and putPosition < 0:
        position = putPosition + callPosition
    elif putPosition < 0:
        position = callPosition - premTotal
    elif callPosition < 0:
        position = putPosition - premTotal

# TODO Check the if statements for straddle calculation, concern on the second elif

    # And print it
    print('The current position of the strategy is $' + str(position) + '.')


# Strangle, holding a call and a put on the same asset with different strike prices, same expiration date.
# Good if thought that the underlying security will move in price do not know the direction.
# TODO Long straddle calculation.
# TODO Start short straddle.
# DONE Checks to see if the strike prices are correct for the strategy


def strangle():
    callStrike = pyip.inputNum('Enter the strike price of the call: ')
    putStrike = pyip.inputNum('Enter the strike price of the put: ')
    currentPrice = pyip.inputNum('Enter the current price of the stock: ')
    premiumPaid = pyip.inputNum('Enter the total premium paid for the strategy: ')

    # Going long or short?
    choice = pyip.inputMenu(['long', 'short'], numbered=True)
    # What to do if long or short.
    if choice == 'long':
        print("A long strangle involves buying an out of the money call and an out of the money put."
              "\nThe call option's strike price is higher than the asset's price, and the put's is lower."
              "\nRisk is limited to the premium paid for the option")
        if callStrike < currentPrice:
        print('The strangle will not work as the strike price of the call option should be higher than the asset price.')
        if putStrike > currentPrice:
        print('The strangle will not work as the strike price of the put option should be lower than the asset price.')

        callStanding = callStrike - currentPrice
        putStanding = putStrike - currentPrice  # check this for some reason I cannot do the random mental math rn.

        currentLongPosition = callStanding + putStanding - premiumPaid

        print('The current position in the strategy is ' + str(currentLongPosition) + '.')

    elif choice == 'short':
        print(
            'A short strangle involves the sale of an out of the money put and an out of the money call. Strategy is '
            '\noverall neutral and limited potential for profit. Profit occurs when the strike price of the underlying '
            '\nstock trades in a narrow range between the two break even points. Max profit is net premium received for '
            '\nwriting the two options.')
        # need to get inputs for selling the options
        callIncome = pyip.inputNum('Enter the sell price of the written call: ')
        putIncome = pyip.inputNum('Enter the sell price of the written put: ')
        wroteIncome = callIncome + putIncome
        callStanding = callStrike - currentPrice
        putStanding = putStrike - currentPrice  # check this for some reason I cannot do the random mental math rn.
        # TODO Check short strangle calculation.
        currentLongPosition = wroteIncome - callStanding - putStanding

# TODO Add iron condor calculation.
# oh my god this is complicated

def ironCondor:
    # Get the necessary inputs for the four options.
    currentPrice = pyip.inputNum('Enter the current price of the underlying asset: ')
    print('First, buy one out of the money put with a strike price below the current price of the asset.')
    otmPutStrike = pyip.inputNum('Enter the strike price of that call option: ', lessThan=currentPrice)
    otmPutPrice = pyip.inputNum('Enter the price paid for that put: ')
    print('Next, sell one OTM or ATM put with a strike price near the current price of the underlying asset.')
    otmatmPutStrike = pyip.inputNum('Enter the strike price of the OTM or ATM put sold: ')
    otmatmPutIncome = pyip.inputNum('Enter the income from selling that put: ')
    print('Next, sell one OTM or ATM call with a strike price above the current price of the underlying asset.')
    otmatmCallStrike = pyip.inputNum('Enter the strike price of that call: ', greaterThan=currentPrice)
    otmatmCallIncome = pyip.inputNum('Enter the income from selling that call: ')
    print('Finally, buy an OTM call with a strike price further above the current price of the asset.')
    furtherOTMCallStrike = pyip.inputNum('Enter the strike price of that OTM call: ', greaterThan=otmatmCallStrike)
    furtherOTMCallPrice = pyip.inputNum('Enter the price paid for that call: ')

    ironCondorCredit = otmatmCallIncome - furtherOTMCallPrice + otmatmPutIncome - otmPutPrice
    print('The maximum profit of the strategy is ' + str(ironCondorCredit))
    # TODO Iron condor price movement affecting profit.

    if currentPrice > otmPutStrike and currentPrice < otmatmCallStrike:
        standing = ironCondorCredit
        print('The profit has been maximized and comes out to $' + ironCondorCredit + '.')
    elif currentPrice > furtherOTMCallStrike and currentPrice < otmPutStrike:
        standing =   # max loss

# DONE Fix invalid syntax line 246

option = pyip.inputMenu(
    ['call', 'put', 'covered call', 'married put', 'credit spread', 'debit spread', 'straddle', 'strangle', 'q'],
    numbered=True)

if option == 'call':
    print('Call option selected.')
    time.sleep(startSleep)
    print('A call option gives an investor the right, but not the obligation, to buy a stock at a certain price, '
          '\nthe strike price.')
    time.sleep(definitionSleep)
    print('Starting call option calculation.')
    time.sleep(execSleep)
    callCalc()
elif option == 'put':
    print('Put option selected.')
    time.sleep(startSleep)
    print('A put option gives an investor the right, but not the obligation, to sell a stock at a certain price, '
          '\nthe strike price.')
    time.sleep(execSleep)
    print('Starting put option calculation.')
    putCalc()
elif option == 'covered call':
    print('Covered call strategy selected.')
    time.sleep(startSleep)
    print('A covered call is a transaction where an investor sells a call option and owns the equivalent amount of '
          '\nthe underlying security. To execute, the investor is long the asset then sells calls on the same asset to '
          '\ngenerate income. This is a neutral strategy, meaning the investor only expects a minor increase in the '
          '\nunderlying stock price of the written call option. Usually employed if an investor wants to hold the '
          '\nstock for a long time but does not expect near term appreciation, so generates income from the option '
          '\npremium.')
    time.sleep(execSleep)
    print('Starting the calculation of a covered call.')
    coveredCall()
elif option == 'married put':
    print('Married put strategy selected.')
    time.sleep(startSleep)
    print('A married put is a strategy where an investor is long the asset and purchases an at the money put option '
          '\non the same asset to protect against depreciation of said asset. The investor essentially protects against '
          '\nthe downside risk yet can still participate in any gains from the upside. ')
    time.sleep(execSleep)
    print('Starting the calculation of a married put.')
    marriedPut()
elif option == 'credit spread':
    print('Credit spread selected.')
    time.sleep(startSleep)
    print('A credit spread involves the sale of a high premium option followed by the purchase of a lower premium '
          '\noption. Premium received from writing is greater than purchasing, resulting in a premium. This is the '
          '\nmaximum profit.')
    time.sleep(execSleep)
    print('Starting the credit spread calculation.')
    creditSpread()
elif option == 'debit spread':
    print('Debit spread selected.')
    time.sleep(startSleep)
    print('A debit spread involves buying a high premium option and then selling an option at a lower premium. This '
          '\nresults in a premium paid by the investor. Used to offset the costs associated with owning long options '
          '\npositions.')
    time.sleep(execSleep)
    print('Starting the debit spread calculation.')
    debitSpread()
elif option == 'straddle':
    print('Straddle selected.')
    time.sleep(startSleep)
    print('A straddle involves the purchase of a put and a call at the same strike price and expiration date. Profit '
          '\noccurs when the stock rices or falls more than the premium paid on the strategy. Profit potential is '
          '\nunlimited.')
    time.sleep(execSleep)
    print('Starting the straddle calculation.')
    straddle()
elif option == 'strangle':
    print('Strangle selected.')
    time.sleep((startSleep))
    print('A strangle is a strategy where an investor owns a call and a put option, each having different strike '
          '\nprices, on the same asset and each having the same expiration date. This strategy works well when when an '
          '\ninvestor expects a large price movement in the near future, but unsure of the direction. Profitable with '
          '\nsharp swings.')
    time.sleep(execSleep)
    print('Starting the strangle calculation.')
    time.sleep(execSleep)
    strangle()
elif option == 'iron condor':
    print("Iron condor selected. That's metal AF.")
    time.sleep((startSleep))
    print('An iron condor is a strategy consisting of four options, two calls (one short one long) and two puts (one '
          '\nshort one long), along with four different strike prices and same expiration date. The strategy profits'
          '\nfrom low volatility in the underlying asset. Profit is maximized when the underlying asset closes between'
          '\nthe middle strike prices at expiration.')
    time.sleep(execSleep)
    ironCondor()
elif option == 'q':
    time.sleep(execSleep)
    print('lol q is not a strategy, you just stopped the program.')
    sys.exit()
