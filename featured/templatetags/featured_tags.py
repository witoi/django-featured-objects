from django import template
from django.contrib.contenttypes.models import ContentType

from ..models import Category, Featured


register = template.Library()


@register.filter(name='featured_category_perm')
def featured_category_perm(user, category_slug):
    try:
        category = Category.objects.get(slug=category_slug)
        return user.has_perm('featured.change_category', category)
    except Category.DoesNotExist:
        return False


@register.filter(name='is_featured_in')
def is_featured_in(obj, category_slug):
    try:
        category = Category.objects.get(slug=category_slug)
        content_type = ContentType.objects.get_for_model(obj)
        return Featured.objects.filter(content_type=content_type, object_id=obj.id, category=category).exists()
    except Category.DoesNotExist:
        return False
