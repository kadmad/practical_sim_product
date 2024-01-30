# Create your tasks here

from product.models import Product, Category
from faker import Faker
from celery import shared_task
import random


@shared_task
def populate_products(count):
    faker = Faker()
    product_objs = []
    categories = [Category(name=faker.name()) for _ in range(20)]
    Category.objects.bulk_create(categories)
    for _ in range(count):
        product_objs.append(
            Product(
                category=random.choice(categories),
                title=faker.name(),
                description=faker.city(),
                price=random.choice(range(1000, 5000)),
                status=random.choice([True, False]),
            )
        )
    Product.objects.bulk_create(product_objs)
    return product_objs
