from django.test import TestCase
from django.db import IntegrityError
from django.http import Http404
from django.contrib.auth.models import User

from featured.models import Featured, Category, get_featured_queryset_for
from featured.views import FeaturedListView


class FeaturedModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Joe')
        self.user2 = User.objects.create(username='Doe')
        self.category = Category.objects.create(slug='category', active=True)
        self.category2 = Category.objects.create(slug='category2', active=True)

    def test_create_without_category(self):
        self.assertRaises(IntegrityError, Featured.objects.create, content_object=self.user)

    def test_create(self):
        featured = Featured.objects.create(content_object=self.user, category=self.category)
        self.assertIsInstance(featured, Featured)
        self.assertEqual(featured.content_object, self.user)

    def test_generic_queryset(self):
        featured = Featured.objects.create(content_object=self.user, category=self.category)
        featured = Featured.objects.create(content_object=self.user2, category=self.category2)

        manager = get_featured_queryset_for(User)

        self.assertEqual(list(manager.all().order_by('pk')), [self.user, self.user2])

    def test_generic_queryset_for_category(self):
        featured = Featured.objects.create(content_object=self.user, category=self.category)
        featured = Featured.objects.create(content_object=self.user2, category=self.category2)

        manager = get_featured_queryset_for(User, category=self.category)

        self.assertEqual(list(manager.all()), [self.user])


class CategoryModelTest(TestCase):
    def test_create(self):
        category = Category.objects.create(slug='category')

        self.assertIsInstance(category, Category)
        self.assertIsNotNone(category.pk)
        self.assertFalse(category.active)

    def test_create_same_slug(self):
        Category.objects.create(slug='category')

        category = Category(slug='category')
        self.assertRaises(IntegrityError, category.save)

    def test_create_active_true(self):
        category = Category.objects.create(slug='category', active=True)

        self.assertTrue(category.active)


class CategoryFeaturedTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(slug='category-slug', active=True)
        self.user1 = User.objects.create(username='joe1')
        self.user2 = User.objects.create(username='joe2')
        self.user3 = User.objects.create(username='joe3')
        Featured.objects.create(content_object=self.user1, category=self.category)
        Featured.objects.create(content_object=self.user2, category=self.category)

    def test_get_context_data_when_inactive_category(self):
        self.category.active = False
        self.category.save()
        view = FeaturedListView()

        self.assertRaises(Http404, view.get_context_data, slug=self.category.slug, model='auth.user')

    def test_get_context_data_when_inexistent_category_slug(self):
        view = FeaturedListView()

        self.assertRaises(Http404, view.get_context_data, slug='inexistent-cateogry-slug', model='auth.user')

    def test_get_context_data_when_inexistent_model(self):
        view = FeaturedListView()

        self.assertRaises(Http404, view.get_context_data, slug=self.category.slug, model='auth.inexistentmodel')

    def test_get_context_data(self):
        view = FeaturedListView()
        queryset = get_featured_queryset_for(User, category=self.category)

        context = view.get_context_data(self.category.slug, 'auth.user')

        self.assertEqual(2, len(context))
        self.assertTrue('object_list' in context)
        self.assertEqual(list(queryset), list(context['object_list']))
        self.assertTrue('user_list' in context)
        self.assertEqual(list(queryset), list(context['user_list']))

    def test_get_category_template_names(self):
        view = FeaturedListView()
        view.get_context_data(self.category.slug, 'auth.user')
        expected = 'featured/%(slug)s_featured_list.html' % {'slug': self.category.slug}

        result = view.get_category_template_name()

        self.assertEqual(expected, result)

    def test_get_template_names(self):
        view = FeaturedListView()
        view.get_context_data(self.category.slug, 'auth.user')
        expected = ['featured/%(slug)s_featured_list.html' % {'slug': self.category.slug},
                    'featured/featured_list.html']

        result = view.get_template_names()

        self.assertEqual(expected, result)
