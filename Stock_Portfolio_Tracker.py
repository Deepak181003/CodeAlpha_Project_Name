import yfinance as yf

portfolio = {}

def add_stock():
    ticker = input("Enter stock symbol (e.g., AAPL): ").upper()
    shares = int(input("Enter number of shares: "))
    if ticker in portfolio:
        portfolio[ticker] += shares
    else:
        portfolio[ticker] = shares

def show_portfolio():
    total = 0.0
    print("\nYour Portfolio:")
    for ticker, shares in portfolio.items():
        stock = yf.Ticker(ticker)
        price = stock.info.get("regularMarketPrice", 0)
        value = price * shares
        print(f"{ticker}: {shares} shares @ ${price:.2f} = ${value:.2f}")
        total += value
    print(f"Total Portfolio Value: ${total:.2f}\n")

while True:
    print("1. Add Stock\n2. Show Portfolio\n3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_stock()
    elif choice == "2":
        show_portfolio()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
