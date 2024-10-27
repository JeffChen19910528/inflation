from fredapi import Fred

# 使用你的API密鑰，從 https://fred.stlouisfed.org/ 註冊獲取API密鑰
fred = Fred(api_key='YOUR_API_KEY')

# 抓取美國CPI數據，CPIAUCSL是美國全城市消費者物價指數的代碼
cpi_data = fred.get_series('CPIAUCSL')

# 打印2023年和2024年的CPI數據
print("2023年美國CPI數據: ", cpi_data['2023-01-01':'2023-12-31'])
print("2024年美國CPI數據: ", cpi_data['2024-01-01':'2024-12-31'])