import yfinance as yf
import matplotlib
import matplotlib.pyplot as plt

stock = "GOOG"
google = yf.Ticker(stock)

stockData = google.info

print("=====================================================")
print("#################### " + stock + "###################")
print("=====================================================")

print("website : ",stockData['website'])

print("regularMarketPrice : ",stockData['regularMarketPrice'])

print("regularMarketOpen : ",stockData['regularMarketOpen'])

print("twoHundredDayAverage : ",stockData['twoHundredDayAverage'])

print("fiftyDayAverage : ",stockData['fiftyDayAverage'])

print("averageDailyVolume10Day : ",stockData['averageDailyVolume10Day'])

print("averageVolume10days : ",stockData['averageVolume10days'])

print("regularMarketDayHigh : ",stockData['regularMarketDayHigh'])

print("regularMarketDayLow : ",stockData['regularMarketDayLow'])

print("trailingPE : ",stockData['trailingPE'])

print("fiftyTwoWeekHigh : ",stockData['fiftyTwoWeekHigh'])

print("fiftyTwoWeekLow : ",stockData['fiftyTwoWeekLow'])

print("52WeekChange : ",stockData['52WeekChange'])

print("bookValue : ",stockData['bookValue'])

print("bookValue : ",stockData['bookValue'])

print("=====================================================")
print("#################### HISTORY ###################")
print("=====================================================")
df = google.history(period='1d', interval="1m")
print(df)

print("=====================================================")
print("#################### MULTIPLE STOCKS ###################")
print("=====================================================")
data = yf.download("GOOG", start="2021-01-01", end="2021-03-12", group_by='tickers')
print(data)

print("=====================================================")
print("#################### HISTORY LOW ###################")
print("=====================================================")
df = google.history(period='1d', interval="1m")

# df = df[['Low']]
# df.head()
# print(df)

# X = df.index.values
# y = df['Low'].values

# # The split point is the 10% of the dataframe length
# offset = int(0.10*len(df))
# X_train = X[:-offset]
# y_train = y[:-offset]
# X_test  = X[-offset:]
# y_test  = y[-offset:]



ticker = yf.Ticker('GOOG')
tsla_df = ticker.history(period="max")
print(tsla_df)
tsla_df['Close'].plot(title="Google stock price")
plt.show()
