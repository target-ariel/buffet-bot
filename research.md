# Buffet Bot Research: Target Assets

This project focuses on identifying ETFs and stocks that align with Warren Buffett's value/quality principles, filtered for availability on InvestEngine, and ranked using a geometric growth model for 3-12 month outlooks.

## Potential ETF Candidates (InvestEngine Available)

| Ticker | Name | Why it fits |
| --- | --- | --- |
| VUSA | Vanguard S&P 500 UCITS ETF | Buffett's #1 recommendation for most. |
| IWFQ | iShares Edge MSCI World Quality Factor | Focuses on high ROE, low debt, and stable earnings. |
| VVAL | Vanguard Global Value Factor | Pure value play based on financials. |
| MOTU | VanEck US Wide Moat UCITS ETF | Tracks companies with sustainable competitive advantages (Moats). |
| GGRP | WisdomTree Global Quality Dividend Growth | Quality + Dividend growth. |

## Geometric Model Principles

The "Twist" involves using a geometric Brownian motion (GBM) or a simpler geometric compounding model to project returns based on:
1.  **Fundamental Score:** (ROE * Profit Margin) / (Debt/Equity).
2.  **Momentum/Volatility Overlay:** Adjusting the 3-12 month timeframe using current volatility.

## Next Steps
- [ ] Verify exact IE availability for MOTU/MUKG.
- [ ] Pull underlying holdings for top 3 ETFs.
- [ ] Create financial analysis script.
