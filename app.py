import json  # unused import: flake8 will flag F401
import json  # unused import: flake8 will flag F401
"""ShopKart API: a tiny product catalogue service used through the DevOps course."""
import os

from flask import Flask, jsonify

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Diwali Lamp Set", "price": 499},
    {"id": 2, "name": "Silk Saree", "price": 2999},
    {"id": 3, "name": "Brass Diya", "price": 249},
]


@app.get("/health")
def health():
    return jsonify(status="ok", version=os.getenv("APP_VERSION", "dev"))


@app.get("/products")
def list_products():
    return jsonify(PRODUCTS)


@app.get("/products/<int:product_id>")
def get_product(product_id):
    item = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if item is None:
        return jsonify(error="product not found"), 404
    return jsonify(item)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
