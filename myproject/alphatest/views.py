
from alpha_vantage.timeseries import TimeSeries
from django.shortcuts import render
import itertools
import json
import pandas
from django.http import HttpResponse, JsonResponse



def index(request):
    ts = TimeSeries(key='J13PMOT141Q8ZY1S', output_format='pandas')
    data, meta_data = ts.get_monthly(symbol='NSE:VEDL')
    chartData = data[['1. open', '2. high', '3. low', '4. close']]
    #volumeData = data[['5. volume']]
    date = data.index.tolist()
    newChartData = chartData.values.tolist()

    for i, j in itertools.zip_longest(date, newChartData):
        j.insert(0, i)
    return render(request, "index/alpha.html", {'newChartData': newChartData})
#    return HttpResponse(json.dumps(data), content_type='application/json')
