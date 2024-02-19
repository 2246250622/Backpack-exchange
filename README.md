# Backpack 交易所刷交易量脚本

如果你还没有注册，可以通过一下链接去注册：https://backpack.exchange/refer/51bitquant

刷交易量获得打新空投的机会， 最近传言 Backpack 要上Wormhole或者Tensor的IDO/IEO项目。

# 如何使用

1. 下载代码，安装相应的依赖库： pip install -r requirements.txt

2. 注册backpack交易所：https://backpack.exchange/refer/51bitquant , 然后实名验证
3. 从币安或者其他交易所充值到backpack
4. 申请apikey: https://backpack.exchange/settings/api-keys
5. 配置交易参数 具体参数在 config.py 文件
```
api_key = "你的api key"
api_secret = "你的api secret"

trade_quantity = 3  # 交易的下单数量.
vol_precision = 2  # 数量精度， 保留两位小数.
trading_fee = 0.001  # 千分之手续费.
trade_pair = "SOL_USDC"  # 交易对.
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
刷交易量会有手续费和滑点的损耗，滑点比较下，主要是手续费, 千分之1手续费的损耗, 滑点相对较小， 交易SOL_UDSC 滑点在万一以下下。
另外， 改脚本只是用户刷简道的刷交易量，博取空投的或者打新的分配额度。具体请看代码。使用前，请注意风险。

# 联系方式：
项目中缺少backpack_client.py 文件
获得方式， 通过邀请链接注册：https://backpack.exchange/refer/51bitquant
或者付费购买， 需要该代码可以联系微信： bitquant51





