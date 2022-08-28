from store.models import Category, Product


def get_all_category():
    return Category.objects.all()
    
def get_all_products():
    return Product.objects.all()
