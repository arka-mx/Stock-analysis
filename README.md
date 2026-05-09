This is my stock analysis project# 📈 Stock Analysis — Sector Correlation Framework

A Python project focused on analyzing how major US market sectors move relative to each other using sector ETFs.

The project studies:

* Correlations between sectors
* Beta-adjusted returns
* Relative sector movements
* Diversification behavior during market stress

---

## 🏛️ Sector ETFs Used

| Sector                 | ETF  |
| ---------------------- | ---- |
| Technology             | XLK  |
| Financials             | XLF  |
| Healthcare             | XLV  |
| Energy                 | XLE  |
| Industrials            | XLI  |
| Consumer Staples       | XLP  |
| Consumer Discretionary | XLY  |
| Utilities              | XLU  |
| Materials              | XLB  |
| Real Estate            | XLRE |
| Communication Services | XLC  |

---

## ⚙️ Features

✅ Historical market data collection
✅ Daily return calculations
✅ Correlation matrix generation
✅ Correlation strength classification
✅ Beta-based decorrelation
✅ Relative return spread analysis

---

## 📊 Correlation Classification

| Correlation          | Strength |
| -------------------- | -------- |
| |corr| ≥ 0.65        | Strong   |
| 0.40 ≤ |corr| < 0.65 | Moderate |
| |corr| < 0.40        | Weak     |

---

## 🧠 Main Insight

Low historical correlation does **not** guarantee diversification.

During periods of:

* liquidity stress,
* macroeconomic shocks,
* or panic selling,

multiple sectors can suddenly become highly correlated.

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* yFinance

---

## 🚀 Installation

```bash id="xv1nla"
git clone https://github.com/arka-mx/Stock-analysis.git
cd Stock-analysis
pip install pandas numpy yfinance
python main.py
```

---

## 📚 Related Links

### Medium Article

[Read the Full Article](https://medium.com/@somap982/sector-correlations-are-not-static-a-small-experiment-with-us-sector-etfs-8fc02e550317?utm_source=chatgpt.com)

### GitHub Repository

[Project Repository](https://github.com/arka-mx/Stock-analysis?utm_source=chatgpt.com)
