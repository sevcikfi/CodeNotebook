"""

"""
import pandas as pd

def download_data(days=365):
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI()
    return  cg.get_coin_market_chart_by_id(id="monero", vs_currency="usd", days=days,interval="daily")

def parse_json(raw_json):
    prices = pd.json_normalize(raw_json, record_path=["prices"]).set_axis(["time","price"], axis="columns")
    market_caps = pd.json_normalize(raw_json, record_path=["market_caps"]).set_axis(["time","market_caps"], axis="columns")
    total_volumes = pd.json_normalize(raw_json, record_path=["total_volumes"]).set_axis(["time","total_volumes"], axis="columns")
    merged = pd.merge(pd.merge(prices, market_caps), total_volumes)
    merged["time"] = pd.to_datetime(merged["time"], unit='ms').apply(lambda t: t.strftime('%Y-%m-%d'))
    return merged.set_index("time")
    
if __name__ == "__main__":
    js = download_data()
    data = parse_json(js)

    print(data)
    print(data.describe())
    print(data.info())

    data.to_csv("monero.csv")
    
    #TODO: look for csv and then call the server
    #TODO: rolling average function (7d, 14d, 1m, 6m, 1y)
    #TODO: maybe graf it all?