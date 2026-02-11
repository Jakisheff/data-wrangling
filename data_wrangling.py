#!/usr/bin/env python
# coding: utf-8

# # Data Wrangling Exercises

# ## Exercise 1: Concatenate

# In[ ]:


import pandas as pd
import numpy as np
from tabulate import tabulate

df1 = pd.DataFrame([['a', 1], ['b', 2]],
                   columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 1], ['d', 2]],
                   columns=['letter', 'number'])

df_concat = pd.concat([df1, df2], ignore_index=True)
print(df_concat.to_markdown())


# ## Exercise 2: Merge

# In[ ]:


#df1

df1_dict = {
        'id': ['1', '2', '3', '4', '5'],
        'Feature1': ['A', 'C', 'E', 'G', 'I'],
        'Feature2': ['B', 'D', 'F', 'H', 'J']}

df1 = pd.DataFrame(df1_dict, columns = ['id', 'Feature1', 'Feature2'])

#df2
df2_dict = {
        'id': ['1', '2', '6', '7', '8'],
        'Feature1': ['K', 'M', 'O', 'Q', 'S'],
        'Feature2': ['L', 'N', 'P', 'R', 'T']}

df2 = pd.DataFrame(df2_dict, columns = ['id', 'Feature1', 'Feature2'])

# Question 1: Inner Merge
df_merge_inner = pd.merge(df1, df2, on='id')
print("Inner Merge Results:")
print(df_merge_inner.to_markdown())

# Question 2: Outer Merge with Suffixes
df_merge_outer = pd.merge(df1, df2, on='id', how='outer', suffixes=('_df1', '_df2'))
print("\nOuter Merge Results:")
print(df_merge_outer.to_markdown())


# ## Exercise 3: Merge MultiIndex

# In[ ]:


#generate days
all_dates = pd.date_range('2021-01-01', '2021-12-15')
business_dates = pd.bdate_range('2021-01-01', '2021-12-31')

#generate tickers
tickers = ['AAPL', 'FB', 'GE', 'AMZN', 'DAI']

# create indexes
index_alt = pd.MultiIndex.from_product([all_dates, tickers], names=['Date', 'Ticker'])
index = pd.MultiIndex.from_product([business_dates, tickers], names=['Date', 'Ticker'])

# create DFs
np.random.seed(42)
market_data = pd.DataFrame(index=index,
                        data=np.random.randn(len(index), 3),
                        columns=['Open','Close','Close_Adjusted'])

alternative_data = pd.DataFrame(index=index_alt,
                                data=np.random.randn(len(index_alt), 2),
                                columns=['Twitter','Reddit'])

# Merge alternative_data on market_data
merged_df = market_data.merge(alternative_data, how='left', left_index=True, right_index=True)
merged_df_filled = merged_df.fillna(0)

print(f"Shape: {merged_df_filled.shape}")
print(merged_df_filled.head().to_markdown())

# Verify Question 2 condition
print(f"Correct Fill Check: {merged_df_filled.sum().sum() == merged_df.sum().sum()}")


# ## Exercise 4: Groupby Apply

# In[ ]:


def winsorize(df_series, quantiles):
    """
        df: pd.DataFrame or pd.Series
        quantiles: list [0.05, 0.95]

    """
    if isinstance(df_series, pd.DataFrame):
         df_series = df_series.iloc[:, 0]

    min_value = df_series.quantile(quantiles[0])
    max_value = df_series.quantile(quantiles[1])

    return df_series.clip(lower = min_value, upper = max_value)

df = pd.DataFrame(range(1,11), columns=['sequence'])
print(winsorize(df, [0.20, 0.80]).to_markdown())


groups = np.concatenate([np.ones(10), np.ones(10)+1,  np.ones(10)+2, np.ones(10)+3, np.ones(10)+4])
df_grouped = pd.DataFrame(data= zip(groups,
                            range(1,51)),
                columns=["group", "sequence"])

result = df_grouped.groupby("group")['sequence'].apply(lambda x: winsorize(x, [0.05, 0.95]))
print(result.head(11).to_markdown())


# ## Exercise 5: Groupby Agg

# In[ ]:


df_agg = pd.DataFrame({
    'value': [20.45, 22.89, 32.12, 111.22, 33.22, 100, 99.99],
    'product': ['table', 'chair', 'chair', 'mobile phone', 'table', 'mobile phone', 'table']
})

agg_result = df_agg.groupby('product').agg({'value':['min','max','mean']})
print(agg_result.to_markdown())


# ## Exercise 6: Unstack

# In[ ]:


business_dates = pd.bdate_range('2021-01-01', '2021-12-31')

#generate tickers
tickers = ['AAPL', 'FB', 'GE', 'AMZN', 'DAI']

#create indexs
index = pd.MultiIndex.from_product([business_dates, tickers], names=['Date', 'Ticker'])

# create DFs
market_data = pd.DataFrame(index=index,
                        data=np.random.randn(len(index), 1),
                        columns=['Prediction'])

unstacked_df = market_data.unstack()
print(unstacked_df.head().to_markdown())

try:
    import matplotlib.pyplot as plt
    unstacked_df.plot(title = 'Stocks 2021')
    plt.savefig('stocks_2021.png')
    print("Plot saved to stocks_2021.png")
except ImportError:
    print("Matplotlib not installed or failed to verify plot")

