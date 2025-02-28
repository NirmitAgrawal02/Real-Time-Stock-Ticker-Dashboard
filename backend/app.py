from fastapi import FastAPI
import requests

app = FastAPI()
API_KEY = "YOUR_ALPHA_VANTAGE_KEY"

@app.get("/stock/{symbol}")
async def get_stock(symbol: str):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={API_KEY}"
    response = requests.get(url).json()
    latest = response["Time Series (1min)"][list(response["Time Series (1min)"].keys())[0]]
    return {"symbol": symbol, "price": float(latest["4. close"])}