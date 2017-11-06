import pandas as pd
import numpy as np
from fbprophet import Prophet
import matplotlib.pyplot as plt

df = pd.read_csv('prices2pages.csv')
df['y'] = np.log(df['y'])

df.head(n=3000)
print(df.head(n=3000))

m = Prophet()
m.fit(df)


future = m.make_future_dataframe(periods=60)
future.tail()

forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

m.plot(forecast);
m.plot_components(forecast);
plt.show()
