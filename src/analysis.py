import pandas as pd
import numpy as np


def calculate_metrics(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate historical performance and volatility metrics.
    """

    df = data.copy()

    # Daily percentage returns
    df["Daily Return"] = df["Close"].pct_change()

    # Moving averages
    df["MA 20"] = df["Close"].rolling(window=20).mean()
    df["MA 50"] = df["Close"].rolling(window=50).mean()

    # Annualized rolling volatility (based on 252 trading days)
    df["Volatility 20"] = (
        df["Daily Return"]
        .rolling(window=20)
        .std()
        * np.sqrt(252)
    )

    return df


if __name__ == "__main__":
    from data_loader import load_stock_data

    ticker = "NVDA"

    stock_data = load_stock_data(ticker)
    analyzed_data = calculate_metrics(stock_data)

    print(f"\nMarketLab Analysis: {ticker}")
    print("=" * 50)

    print("\nLatest metrics:")
    print(analyzed_data[
        ["Close", "Daily Return", "MA 20", "MA 50", "Volatility 20"]
    ].tail())

    latest = analyzed_data.iloc[-1]

    print("\nLatest calculated values:")
    print(f"Closing price: ${latest['Close']:.2f}")
    print(f"Daily return: {latest['Daily Return']:.2%}")
    print(f"20-day moving average: ${latest['MA 20']:.2f}")
    print(f"50-day moving average: ${latest['MA 50']:.2f}")
    print(f"20-day annualized volatility: {latest['Volatility 20']:.2%}")