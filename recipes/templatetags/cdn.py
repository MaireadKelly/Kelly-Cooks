# recipes/templatetags/cdn.py
from django import template

register = template.Library()

@register.filter
def cl_transform(url, transform):
    """
    Insert a Cloudinary transformation right after '/upload/'.
    Example:
      {{ recipe.image.url|cl_transform:"f_auto,q_auto,c_fill,g_auto,w_480,h_360" }}
    """
    if not url:
        return url
    marker = "/upload/"
    pos = url.find(marker)
    if pos == -1:
        return url  # not a Cloudinary delivery URL
    # Keep anything after /upload/ (including version v123...)
    return url[:pos + len(marker)] + transform + "/" + url[pos + len(marker):]
