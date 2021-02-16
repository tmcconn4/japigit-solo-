#import urllib.request
#import sys
#import pandas as pd
from alpha_vantage.timeseries import TimeSeries

KEY='V9G610PD81VVQJEO'


def getStockdata(symbol):
  try:
    ts = TimeSeries(key=KEY, output_format='pandas')

    data, meta_data = ts.get_intraday(symbol=symbol, interval='5min')
    return str(data.tail(1).iloc[0]['4. close'])

  except:
    return "not found"

def main():
  File = open('japi.out', 'w')
  while 1:
    userInput = input('Enter stock symbol or exit to exit: ').upper()
    if userInput != 'Exit':
      serverData = 'The current price of {} is {} \n'.format(userInput, getStockdata(userInput))
      print(serverData)
      File.write(serverData)
    else:
      sys.exit('\nThank you for your time!\n')
  File.close()

main()