"""

"""
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

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
    
def load_local(name="monero", extension="csv"):
    if "." in name:
        path = name
    else:
        path = name + "." + extension
    return pd.read_csv(path)


if __name__ == "__main__":
    #js = download_data(2250)
    #data = parse_json(js)
    data = load_local()

    print(data)
    print(data.describe())
    print(data.info())

    #data.to_csv("monero.csv")
    x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in data["time"]]
    y = data["price"].to_numpy()
    plt.plot(x, y)
    plt.savefig("monero",dpi=1000)


    #TODO: look for csv and then call the server
    #TODO: rolling average function (7d, 14d, 1m, 6m, 1y)
    #TODO: maybe graf it all?