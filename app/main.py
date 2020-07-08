# from iexfinance.refdata import get_symbols
# from iexfinance.stocks import Stock

# a = Stock("AAPL")
# print(a.get_quote())


# HISTORICAL DATA
# from datetime import datetime

# from iexfinance.stocks import get_historical_data

# start = datetime(2017, 1, 1)

# end = datetime(2018, 1, 1)

# df = get_historical_data("TSLA", start, end)


# GET INTRADAY DATA
import datetime
import requests_cache

from iexfinance.stocks import (
    Stock,
    get_historical_intraday,
    get_collections,
    get_market_gainers,
    get_market_most_active,
)

# SET UP CACHE
expiry = datetime.timedelta(days=3)
session = requests_cache.CachedSession(
    cache_name="stock-data", backend="sqlite", expire_after=expiry
)

# date = datetime.datetime(2019, 5, 10)

# print(get_historical_intraday("AAPL", session=session))
# print(get_collections("Computer Hardware", output_format="pandas").head())
a = get_market_gainers(session=session)
# print(a)
print(a[["previousClose", "latestPrice", "changePercent"]])
b = Stock("MOGU")
b.get_quote(session=session)
print(b.get_quote()[["previousClose", "latestPrice", "changePercent"]])
# print(get_market_most_active())
