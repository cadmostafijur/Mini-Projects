from statistics import linear_regression
import pandas
from sklearn.linear_model import LinearRegression
data=pandas.read_csv('iphone_price.csv')
mos=LinearRegression()
mos.fit(data[['version']],data[['price']])
print(mos.predict([[20]]))