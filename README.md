# Backpack 交易所刷交易量腳本

如果你還沒註冊，可以透過連結去註冊：https://backpack.exchange/refer/51bitquant

刷交易量獲得打新空投的機會， 最近傳言 Backpack 要上Wormhole或Tensor的IDO/IEO專案。

# 如何使用

1. 下載程式碼，安裝對應的依賴函式庫： pip install -r requirements.txt

2. 註冊backpack交易所：https://backpack.exchange/refer/51bitquant , 然後實名驗證
3. 從幣安或其他交易所儲值到backpack
4. 申請apikey: https://backpack.exchange/settings/api-keys
5. 設定交易參數 具體參數在 config.py 文件
```
api_key = "你的api key"
api_secret = "你的api secret"

trade_quantity = 3 # 交易的下單數量.
vol_precision = 2 # 數量精度， 保留兩位小數.
trading_fee = 0.001 # 千分之手續費.
trade_pair = "SOL_USDC" # 交易對.
```

6. 启动 main.py 文件
7. 如果需要代理，可以修改项目下面的api/backpack_client 中的proxies参数.
```python
self.proxies = {
    'http': '',
    'https': ''
}

```
# 注意
刷交易量會有手續費和滑點的損耗，滑點比較下，主要是手續費, 千分之1手續費的損耗, 滑點相對較小， 交易SOL_UDSC 滑點在萬一以下下。
另外， 改腳本只是用戶刷簡道的刷交易量，博取空投的或打新的分配額度。 具體請看代碼。 使用前，請注意風險。





