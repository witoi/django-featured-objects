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
        model_class = self.get_model(model)
        self.category = self.get_category(slug)
        object_name = self.get_object_name(model)

        manager = get_featured_queryset_for(model_class, category=self.category)
        return {'object_list': manager, object_name: manager}

    def get_category(self, slug):
        return get_object_or_404(Category, slug=slug, active=True)

    def get_model(self, model):
        app_label, model_name = model.split('.')
        model_class = get_object_or_404(ContentType, app_label=app_label, model=model_name).model_class()
        return model_class

    def get_object_name(self, model):
        app_label, model_name = model.split('.')
        return '%(model_name)s_list' % {'model_name': model_name}

    def get_category_template_name(self):
        return 'featured/%(slug)s_featured_list.html' % {'slug': self.category.slug}
