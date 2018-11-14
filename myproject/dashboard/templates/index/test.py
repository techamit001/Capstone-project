#J13PMOT141Q8ZY1S
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint

import matplotlib.pyplot as plt

ts = TimeSeries(key='J13PMOT141Q8ZY1S')
data, meta_data = ts.get_monthly(symbol='MSFT')
print(meta_data)
print(data)
