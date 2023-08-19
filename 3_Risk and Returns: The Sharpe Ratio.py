# Importing required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Settings to produce nice plots in a Jupyter notebook
plt.style.use('fivethirtyeight')
%matplotlib inline

# Reading in the data
stock_data = pd.read_csv("datasets/stock_data.csv", parse_dates=['Date'], index_col='Date').dropna()
benchmark_data = pd.read_csv("datasets/benchmark_data.csv", parse_dates=['Date'], index_col='Date').dropna()

# Display summary for stock_data
print('Stocks\n')
# ... YOUR CODE FOR TASK 2 HERE ...
stock_data.info()
print(stock_data.head())

# Display summary for benchmark_data
print('\nBenchmarks\n')
# ... YOUR CODE FOR TASK 2 HERE ...
benchmark_data.info()
print(benchmark_data.head())

# visualize the stock_data
# ... YOUR CODE FOR TASK 3 HERE ...
stock_data.plot(title='Stock Data', subplots=True)
stock_data.describe()

# summarize the stock_data
# ... YOUR CODE FOR TASK 3 HERE ...

# plot the benchmark_data
# ... YOUR CODE FOR TASK 4 HERE ...
benchmark_data.plot(title="S&P 500")

# summarize the benchmark_data
# ... YOUR CODE FOR TASK 4 HERE ...
benchmark_data.describe()

# calculate daily stock_data returns
stock_returns = stock_data.pct_change()
stock_returns.plot()
stock_returns.describe()

# plot the daily returns
# ... YOUR CODE FOR TASK 5 HERE ...


# summarize the daily returns
# ... YOUR CODE FOR TASK 5 HERE ...


# calculate daily benchmark_data returns
# ... YOUR CODE FOR TASK 6 HERE ...
sp_returns = benchmark_data['S&P 500'].pct_change()
sp_returns.plot()
sp_returns.describe()

# plot the daily returns
# ... YOUR CODE FOR TASK 6 HERE ...


# summarize the daily returns
# ... YOUR CODE FOR TASK 6 HERE ...


# calculate the difference in daily returns
excess_returns = stock_returns.sub(sp_returns, axis=0)

# plot the excess_returns
# ... YOUR CODE FOR TASK 7 HERE ...
excess_returns.plot()

# summarize the excess_returns
# ... YOUR CODE FOR TASK 7 HERE ...
excess_returns.describe()

# calculate the mean of excess_returns 
# ... YOUR CODE FOR TASK 8 HERE ...
avg_excess_return = excess_returns.mean()

# plot avg_excess_returns
# ... YOUR CODE FOR TASK 8 HERE ...
avg_excess_return.plot.bar(title='Mean of the Return Difference')

# calculate the standard deviations
sd_excess_return = excess_returns.std()

# plot the standard deviations
# ... YOUR CODE FOR TASK 9 HERE ...
sd_excess_return.plot.bar(title='Standard Deviation of the Return Difference')

# calculate the daily sharpe ratio
daily_sharpe_ratio = avg_excess_return.div(sd_excess_return)

# annualize the sharpe ratio
annual_factor = np.sqrt(252)
annual_sharpe_ratio = daily_sharpe_ratio.mul(annual_factor)

# plot the annualized sharpe ratio
# ... YOUR CODE FOR TASK 10 HERE ...
annual_sharpe_ratio.plot.bar(title='Annualized Sharpe Ratio: Stocks vs S&P 500')

# Uncomment your choice.
buy_amazon = True
# buy_facebook = True
