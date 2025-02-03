import yfinance as yahooFinance
 
sbidf = yahooFinance.download(['SBIN.NS'], period='1y')

print(sbidf)