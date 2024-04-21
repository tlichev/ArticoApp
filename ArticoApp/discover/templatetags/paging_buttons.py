from django import template
register = template.Library()

@register.inclusion_tag('', takes_context=True)
def prev_button():

    return {
        'info':'',
        'info2':'',
        'info3':'',
        'info4':'',
    }