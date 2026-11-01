
import yfinance as yf
import pandas as pd


def load_stock_data(
    ticker: str,
    period: str = "1y",
    interval: str = "1d"
) -> pd.DataFrame:
    """
    Download historical stock market data.

    Args:
        ticker: Stock ticker symbol (e.g. NVDA).
        period: Historical period to retrieve.
        interval: Data interval.

    Returns:
        DataFrame containing historical stock data.
    """

    stock = yf.Ticker(ticker)

    data = stock.history(
        period=period,
        interval=interval,
        auto_adjust=True
    )

    if data.empty:
        raise ValueError(f"No historical data found for {ticker}")

    data.index = pd.to_datetime(data.index)

    return data


if __name__ == "__main__":
    df = load_stock_data("NVDA")

    print(df.head())
    print(f"\nRetrieved {len(df)} trading sessions.")
