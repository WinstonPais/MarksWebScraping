from django import template
register = template.Library()

@register.filter(name='ind')
def return_item(l, i):
    try:
        return l[i]
    except:
        return None

@register.filter(name='range')
def return_range(num):
    try:
        return range(num)
    except:
        return None


@register.filter(name='len')
def return_len(lst):
    try:
        return len(lst)
    except:
        return None
