import pandas as pd
import numpy as np
import yfinance as yf


class corr:

    us_sector_etfs = [
        "XLK",
        "XLF",
        "XLV",
        "XLE",
        "XLI",
        "XLP",
        "XLY",
        "XLU",
        "XLB",
        "XLRE",
        "XLC",
    ]

    sector_names = [
        "Technology",
        "Financials",
        "Healthcare",
        "Energy",
        "Industrials",
        "Consumer Staples",
        "Consumer Discretionary",
        "Utilities",
        "Materials",
        "Real Estate",
        "Communication Services",
    ]

    def __init__(self):

        print("Stock analysis of various sectors\n")

        for sector in self.sector_names:
            print(sector)

    def gather_market_data(self):

        data = yf.download(
            tickers=self.us_sector_etfs,
            period="6mo",
            interval="1d"
        )

        return data

    def getting_close_values(self, data):

        close = data["Close"]

        return close

    def calculate_correlations(self, closed_values):

        returns = closed_values.pct_change().dropna()
        print(returns)
        correlation_matrix = returns.corr()

        strong = []
        moderate = []
        weak = []

        cols = correlation_matrix.columns

        for i in range(len(cols)):

            for j in range(i + 1, len(cols)):

                corr_value = correlation_matrix.iloc[i, j]

                pair = (cols[i], cols[j], round(corr_value, 2))

                if abs(corr_value) >= 0.65:
                    strong.append(pair)

                elif abs(corr_value) >= 0.4:
                    moderate.append(pair)

                else:
                    weak.append(pair)

        # print("\nStrong correlations:")
        # print(strong)

        # print("\nModerate correlations:")
        # print(moderate)

        # print("\nWeak correlations:")
        # print(weak)

        return returns

    def decorrelate_returns(self, returns, base_etf="XLK"):

        adjusted_returns = {}
        return_differences = {}

        base_returns = returns[base_etf]

        for etf in self.us_sector_etfs:

            if etf == base_etf:
                continue

            target_returns = returns[etf]

            beta = (
                np.cov(target_returns, base_returns)[0, 1]
                / np.var(base_returns)
            )

            adjusted = target_returns - beta * base_returns

            diff = target_returns - base_returns

            adjusted_returns[etf] = adjusted

            return_differences[f"{etf}-{base_etf}"] = diff

        return adjusted_returns, return_differences

    def display_results(self, adjusted_returns, return_differences):

        print("\nAdjusted Returns:\n")
        print(adjusted_returns)
        for etf, values in adjusted_returns.items():

            print(f"{etf}:")

            print(values)

            print()

        print("\nReturn Differences:\n")

        for pair, values in return_differences.items():

            print(f"{pair}:")

            print(values.head())

            print()


obj = corr()

market_data = obj.gather_market_data()

closed_values = obj.getting_close_values(market_data)

returns = obj.calculate_correlations(closed_values)

adjusted_returns, return_differences = obj.decorrelate_returns(
    returns,
    base_etf="XLK"
)

obj.display_results(adjusted_returns, return_differences)