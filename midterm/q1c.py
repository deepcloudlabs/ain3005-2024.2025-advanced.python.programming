from itertools import groupby

products = [
    {
        "id": "p1",
        "name": "Laptop",
        "price": 1500.00,
        "stock": 20,
        "category": "Electronics",
        "discount": 0.1
    },
    {
        "id": "p2",
        "name": "Tablet",
        "price": 800.00,
        "stock": 30,
        "category": "Electronics",
        "discount": 0.15
    },
    {
        "id": "p3",
        "name": "Smartphone",
        "price": 900.00,
        "stock": 50,
        "category": "Electronics",
        "discount": 0.2
    },
    {
        "id": "p4",
        "name": "Headphones",
        "price": 150.00,
        "stock": 100,
        "category": "Accessories",
        "discount": 0.05
    },
    {
        "id": "p5",
        "name": "Smartwatch",
        "price": 300.00,
        "stock": 40,
        "category": "Wearables",
        "discount": 0.1
    },
    {
        "id": "p6",
        "name": "Camera",
        "price": 1200.00,
        "stock": 15,
        "category": "Electronics",
        "discount": 0.12
    },
    {
        "id": "p7",
        "name": "Printer",
        "price": 200.00,
        "stock": 25,
        "category": "Office Equipment",
        "discount": 0.1
    },
    {
        "id": "p8",
        "name": "Monitor",
        "price": 400.00,
        "stock": 60,
        "category": "Electronics",
        "discount": 0.08
    },
    {
        "id": "p9",
        "name": "Keyboard",
        "price": 50.00,
        "stock": 120,
        "category": "Accessories",
        "discount": 0.03
    },
    {
        "id": "p10",
        "name": "External Hard Drive",
        "price": 100.00,
        "stock": 70,
        "category": "Storage",
        "discount": 0.1
    }
]

def find_highest_discounted_product (product_list: list) -> dict[str, object]:
    return list(map(lambda e: {"category": e[0], "product": max(e[1],key=lambda y: y["discount"])},groupby(sorted(products, key = lambda product: product["category"]),key = lambda product: product["category"])))

for e in find_highest_discounted_product(products):
    print(e["category"],": ",e["product"])