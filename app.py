import pandas as pd


# Import csv file and store data in Pandas DataFrame
df = pd.read_csv('amazon_orders.csv')
df = df.fillna(0)
df['Total Charged'] = df['Total Charged'].str.replace('$','').astype(float)
df['Tax Charged'] = df['Tax Charged'].str.replace('$','').astype(float)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Shipment Date'] = pd.to_datetime(df['Shipment Date'])


# Calculate lifetime total spent
total_spent = df['Total Charged'].sum()
total_spent = '${:,.2f}'.format(total_spent)
print(f'\nThe lifetime total amount spent at Amazon is {total_spent}!!!')

# Calculate average spent per order
average = df['Total Charged'].mean()
average = '${:,.2f}'.format(average)
print(f'Average = {average} per order')

# Calculate lifetime median amount spent
median = df['Total Charged'].median()
median = '${:,.2f}'.format(median)
print(f'Median = {median}')

# Calculate largest amount spent
largest_order = df['Total Charged'].max()
largest_order = '${:,.2f}'.format(largest_order)
print(f'Largest Order = {largest_order}!!!')
# Calculate smallest amount spent
smallest_order = df['Total Charged'].min()
smallest_order = '${:,.2f}'.format(smallest_order)
print(f'Smallest order = {smallest_order}')

# Calculate largest amount spent in a single day
largest_day = df.groupby('Order Date').sum()["Total Charged"]
largest_day = largest_day.max()
largest_day = '${:,.2f}'.format(largest_day)
print(f'The largest amount spent in a single day is {largest_day}')


# Calculate lifetime total tax charged
total_tax = df['Tax Charged'].sum()
total_tax = '${:,.2f}'.format(total_tax)
print(f'\nThe lifetime total amount charged on tax at Amazon is {total_tax}!!!')

# Calculate overall tax rate
tax_rate = round(df['Tax Charged'].sum() / df['Total Charged'].sum(), 2)
tax_rate *= 100
tax_rate = round(tax_rate, 1)
print(f'Overall Tax Rate = {tax_rate}%\n')
