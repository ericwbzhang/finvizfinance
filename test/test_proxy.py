
from finvizfinance.quote import finvizfinance

proxies= {
    "http": "socks5://vqcsmngo:ew335afwazgd@45.146.130.123:5800",
    "https": "socks5://vqcsmngo:ew335afwazgd@45.146.130.123:5800",
}

insider_trade= finvizfinance("NVDA", proxies= proxies).ticker_inside_trader()