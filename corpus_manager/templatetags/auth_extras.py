# Necessary imports
from django import template

# Register the template library
register = template.Library()

# Custom filter to check if user has a specific group
@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

# Custom filter to get attribute value from an object
# @register.filter(name='attr')
# def attr(obj, attr):
#     return getattr(obj, attr)