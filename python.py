# Import required libraries
import pandas as pd
from sqlalchemy import create_engine
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# MySQL database connection details
DATABASE_USER = 'your_username'
DATABASE_PASSWORD = 'your_password'
DATABASE_HOST = 'localhost'
DATABASE_NAME = 'your_database_name'

# Connect to the MySQL database
engine = create_engine(f'mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}')

# Step 1: Query demand data from MySQL
query = """
SELECT date, quantity 
FROM historical_demand 
WHERE product_id = 1 
ORDER BY date
"""
demand_data = pd.read_sql(query, engine)

# Step 2: Prepare the data for time series analysis
demand_data['date'] = pd.to_datetime(demand_data['date'])
demand_data.set_index('date', inplace=True)

# Step 3: Build and fit the ARIMA model
# (1,1,1) order is used for ARIMA, adjust based on data patterns
model = ARIMA(demand_data['quantity'], order=(1, 1, 1))
model_fit = model.fit()

# Step 4: Forecast future demand for the next 30 days
forecast = model_fit.forecast(steps=30)

# Step 5: Plot the historical demand and forecasted demand
plt.figure(figsize=(12, 6))
plt.plot(demand_data.index, demand_data['quantity'], label='Historical Demand')
plt.plot(pd.date_range(start=demand_data.index[-1], periods=31, freq='D')[1:], forecast, label='Forecasted Demand', color='orange')
plt.xlabel('Date')
plt.ylabel('Quantity')
plt.title('Demand Forecast')
plt.legend()
plt.show()

# Close the database connection
engine.dispose()
