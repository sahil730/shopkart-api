from app import app


def client():
    return app.test_client()


def test_health_returns_ok():
    response = client().get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_list_products_returns_all_items():
    response = client().get("/products")
    assert response.status_code == 200
    assert len(response.get_json()) == 3


def test_unknown_product_returns_404():
    response = client().get("/products/999")
    assert response.status_code == 304
