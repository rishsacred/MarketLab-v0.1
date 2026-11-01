
import matplotlib.pyplot as plt

from data_loader import load_stock_data
from analysis import calculate_metrics


def plot_stock_analysis(ticker: str):
    # Load and analyze historical data
    data = load_stock_data(ticker)
    df = calculate_metrics(data)

    # Create three vertically stacked charts
    fig, axes = plt.subplots(
        3, 1,
        figsize=(14, 11),
        sharex=True
    )

    fig.suptitle(
        f"{ticker} - MarketLab Historical Analysis",
        fontsize=16,
        fontweight="bold"
    )

    # 1. Closing price and moving averages
    axes[0].plot(df.index, df["Close"], label="Closing Price")
    axes[0].plot(df.index, df["MA 20"], label="20-Day MA")
    axes[0].plot(df.index, df["MA 50"], label="50-Day MA")

    axes[0].set_title("Price and Moving Averages")
    axes[0].set_ylabel("Price ($)")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # 2. Daily returns
    axes[1].plot(
        df.index,
        df["Daily Return"] * 100,
        label="Daily Return"
    )

    axes[1].axhline(0, linewidth=1)
    axes[1].set_title("Daily Returns")
    axes[1].set_ylabel("Return (%)")
    axes[1].grid(True, alpha=0.3)

    # 3. Rolling volatility
    axes[2].plot(
        df.index,
        df["Volatility 20"] * 100,
        label="20-Day Volatility"
    )

    axes[2].set_title("Rolling Annualized Volatility")
    axes[2].set_ylabel("Volatility (%)")
    axes[2].set_xlabel("Date")
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()

    # Save chart
    output_path = f"reports/{ticker}_analysis.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight")

    print(f"Chart saved to {output_path}")

    plt.show()


if __name__ == "__main__":
    plot_stock_analysis("NVDA")
