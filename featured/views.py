from django.views.generic import TemplateView
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from featured.models import Category, get_featured_queryset_for


class FeaturedListView(TemplateView):
    def get_template_names(self):
        template_name = self.get_category_template_name()
        return [template_name, 'featured/featured_list.html']

    def get_context_data(self, slug, model):
        app_label, model_name = model.split('.')
        model_class = get_object_or_404(ContentType, app_label=app_label, model=model_name).model_class()
        self.category = get_object_or_404(Category, slug=slug, active=True)
        manager = get_featured_queryset_for(model_class, category=self.category)
        object_name = '%(model_name)s_list' % {'model_name': model_name}
        return {'object_list': manager, object_name: manager}

    def get_category_template_name(self):
        return 'featured/%(slug)s_featured_list.html' % {'slug': self.category.slug}
