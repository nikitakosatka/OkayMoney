from django.templatetags.static import static
from django.utils.html import format_html

from ._register import register

@register.simple_tag
def css(css_file):
    return format_html(f"<link rel=\"stylesheet\" href=\"{static('okaymoneyapp/css/' + css_file + '.css')}\">")
