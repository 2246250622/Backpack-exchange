import requests
import json
import hashlib
import hmac
import time
from typing import Dict


class BackpackClient:
    BASE_URL = "https://backpack.exchange/api/v1"

    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret

    def _generate_signature(self, data: Dict[str, str]) -> str:
        sorted_data = sorted(data.items(), key=lambda x: x[0])
        message = '&'.join([f"{key}={value}" for key, value in sorted_data])
        signature = hmac.new(self.api_secret.encode(), message.encode(), hashlib.sha256).hexdigest()
        return signature

    def _request(self, endpoint: str, method: str = "GET", data: Dict[str, str] = None) -> Dict[str, any]:
        url = self.BASE_URL + endpoint
        timestamp = str(int(time.time()))

        payload = {
            "api_key": self.api_key,
            "timestamp": timestamp,
        }

        if data:
            payload.update(data)

        signature = self._generate_signature(payload)
        payload["signature"] = signature

        headers = {
            "Content-Type": "application/json",
        }

        if method == "GET":
            response = requests.get(url, headers=headers, params=payload)
        elif method == "POST":
            response = requests.post(url, headers=headers, data=json.dumps(payload))
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        response_data = response.json()
        return response_data

    def get_order_id(self) -> str:
        endpoint = "/order/id"
        response_data = self._request(endpoint)
        order_id = response_data["order_id"]
        return order_id

    def balances(self) -> Dict[str, Dict[str, str]]:
        endpoint = "/balance"
        response_data = self._request(endpoint)
        balances = response_data["balances"]
        return balances

    def depth(self, symbol: str) -> Dict[str, any]:
        endpoint = f"/depth/{symbol}"
        response_data = self._request(endpoint)
        depth = response_data["depth"]
        return depth

    def place_order(self, symbol: str, side: str, order_type: str, price: str, quantity: str) -> Dict[str, any]:
        endpoint = "/order"
        data = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "price": price,
            "quantity": quantity,
        }
        response_data = self._request(endpoint, method="POST", data=data)
        return response_data