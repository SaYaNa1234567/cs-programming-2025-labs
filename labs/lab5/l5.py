products = {
    "яблоки": 100,
    "бананы": 80,
    "апельсины": 120,
    "груши": 90,
    "киви": 150
    }
min_product = min(products, key=products.get)
max_product = max(products, key=products.get)

print(f"Товар с минимальной ценой: {min_product} - {products[min_product]} руб.")
print(f"Товар с максимальной ценой: {max_product} - {products[max_product]} руб.")
