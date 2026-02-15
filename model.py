import numpy as np

def calculate_buffett_score(roe, debt_to_equity, profit_margin):
    """
    Higher score = better quality/value.
    ROE (Return on Equity) should be high.
    Debt/Equity should be low.
    Profit Margin should be healthy.
    """
    # Simple score: ROE * Profit Margin / (Debt/Equity + 0.1 to avoid div by zero)
    score = (roe * profit_margin) / (debt_to_equity + 0.1)
    return score

def geometric_projection(current_price, expected_return, volatility, months=12):
    """
    Project price using a simplified geometric growth expectation.
    """
    t = months / 12
    # Simplified CAGR-based projection
    projected_price = current_price * np.exp((expected_return - 0.5 * volatility**2) * t)
    return projected_price

if __name__ == "__main__":
    # Example for a 'Quality' company
    roe = 0.20  # 20%
    debt_to_equity = 0.5
    profit_margin = 0.15 # 15%
    
    score = calculate_buffett_score(roe, debt_to_equity, profit_margin)
    print(f"Buffett Score: {score:.2f}")
    
    # Projection
    price = 100
    ret = 0.10 # 10% expected return based on fundamentals
    vol = 0.15 # 15% annual vol
    
    projection = geometric_projection(price, ret, vol, months=6)
    print(f"6-Month Projected Price: {projection:.2f}")
