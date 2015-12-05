# Arbitrage
Trading program that detects cyclic arbitrage opportunities in spot currency exchange market

## Problem
As seen on http://priceonomics.com/jobs/puzzle/ 

## Solution
Currently, uses Bellman-Ford-Moore to find negative weight cycles in currency exchange graph
with weight of edges representing negative of log of exchange rate. Starting with each currency,
output the final value of stake after it has been through the negative edge cycle. If this value is 
greater than stake, arbitrage opportunity has been detected.

## API
uses https://www.exchangerate-api.com/ API to access realtime exchange rates. This program incorporates only
25 currencies since there is a limit on api requests for a free account. To run the code get an API key from this site and run
arbitrage.py, rest is pretty intuitive.

## To Do
Make GUI for this in PyQt.
