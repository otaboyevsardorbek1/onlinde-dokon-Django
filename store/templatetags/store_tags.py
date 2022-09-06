from django import template

from store.business_logic.services import Basket


register = template.Library()

@register.simple_tag()
def get_count_product_basket(request):
    return len(Basket(request))

@register.simple_tag()
def get_request_path(request):
    return request.path