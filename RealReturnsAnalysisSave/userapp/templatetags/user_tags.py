from django import template

register = template.Library()


@register.simple_tag
def get_range(a, b):
    return range(a, b)


@register.simple_tag
def get_split_list(value, split_val):
    print(value.split(str(split_val)))
    return value.split(str(split_val))


@register.filter
def return_list_item(l, i):
    return l[i]
