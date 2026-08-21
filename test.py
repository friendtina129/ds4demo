from datetime import datetime, timedelta
import mariadb
import requests

stock_code = "2330.TW"
url = f"https://query1.finance.yahoo.com/v8/finance/chart/{stock_code}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0.0.0 Safari/537.36"
}

end_time = datetime.now()
start_time = end_time - timedelta(days=30)

params = {
    "period1": int(start_time.timestamp()),
    "period2": int(end_time.timestamp()),
    "interval": "1d",
}

response = requests.get(url, params=params, headers=headers, timeout=20)
response.raise_for_status()

result = response.json()["chart"]["result"][0]
timestamps = result["timestamp"]
quotes = result["indicators"]["quote"][0]

rows = []
for timestamp, opening, closing in zip(
    timestamps, quotes["open"], quotes["close"]
):
    if opening is not None and closing is not None:
        date = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
        rows.append((stock_code, date, opening, closing))

if not rows:
    raise RuntimeError(f"找不到 {stock_code} 最近一個月的價格資料")

connection = mariadb.connect(
    user="root",
    password="1234",
    host="localhost",
    port=3306,
    database="aabb",
)

try:
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS stock_prices (
            id INT AUTO_INCREMENT PRIMARY KEY,
            stock_code VARCHAR(20) NOT NULL,
            trade_date DATE NOT NULL,
            opening_price DECIMAL(12, 4) NOT NULL,
            closing_price DECIMAL(12, 4) NOT NULL,
            UNIQUE KEY unique_stock_date (stock_code, trade_date)
        )
        """
    )
    cursor.executemany(
        """
        INSERT INTO stock_prices (
            stock_code, trade_date, opening_price, closing_price
        ) VALUES (?, ?, ?, ?)
        ON DUPLICATE KEY UPDATE
            opening_price = VALUES(opening_price),
            closing_price = VALUES(closing_price)
        """,
        rows,
    )
    connection.commit()
    print(f"已寫入 {len(rows)} 筆 {stock_code} 價格資料到 stock_prices")
finally:
    connection.close()