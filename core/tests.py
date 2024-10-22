from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Brand, Phone


class BrandModelTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='Samsung', nationality='Korea')

    def test_brand_creation(self):
        self.assertEqual(self.brand.name, 'Samsung')
        self.assertEqual(self.brand.nationality, 'Korea')
        self.assertTrue(isinstance(self.brand, Brand))
        self.assertEqual(str(self.brand), 'Samsung')


class PhoneModelTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='Samsung', nationality='Korea')
        self.phone = Phone.objects.create(brand=self.brand, model='Galaxy S21', price=1000, color='Black', screen_size=6.5, status='new', country_of_manufacture='Korea')

    def test_phone_creation(self):
        self.assertEqual(self.phone.model, 'Galaxy S21')
        self.assertEqual(self.phone.price, 1000)
        self.assertEqual(self.phone.color, 'Black')
        self.assertEqual(self.phone.screen_size, 6.5)
        self.assertEqual(self.phone.status, 'new')
        self.assertEqual(self.phone.country_of_manufacture, 'Korea')
        self.assertTrue(isinstance(self.phone, Phone))
        self.assertEqual(str(self.phone), 'Samsung Galaxy S21')


class PhoneCreateViewTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='Apple', nationality='USA')
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

    def test_add_phone_view_requires_login(self):
        response = self.client.get(reverse('core:add_phone'))
        self.assertNotEqual(response.status_code, 200)  # Should redirect to login page

    def test_add_phone_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('core:add_phone'), {
            'brand': self.brand.id,
            'model': 'iPhone 13',
            'price': 1200,
            'color': 'Silver',
            'screen_size': 6.1,
            'status': 'E',
            'country_of_manufacture': 'China'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Phone.objects.count(), 1)
        self.assertEqual(Phone.objects.first().model, 'iPhone 13')


class PhoneDeleteViewTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='Apple', nationality='USA')
        self.phone = Phone.objects.create(brand=self.brand, model='iPhone 13', price=1200, color='Silver', screen_size=6.1, status='new', country_of_manufacture='China')
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

    def test_delete_phone_view_requires_login(self):
        response = self.client.post(reverse('core:delete_phone', args=[self.phone.id]))
        self.assertNotEqual(response.status_code, 200)  # Should redirect to login page

    def test_delete_phone_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('core:delete_phone', args=[self.phone.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Phone.objects.count(), 0)


class BrandListViewTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='Xiaomi', nationality='China')

    def test_brand_list_view(self):
        response = self.client.get(reverse('core:brand_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Xiaomi')


class PhoneListViewTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='Apple', nationality='USA')
        self.phone = Phone.objects.create(brand=self.brand, model='iPhone 13', price=1200, color='Silver', screen_size=6.1, status='new', country_of_manufacture='China')

    def test_phone_list_view(self):
        response = self.client.get(reverse('core:phone_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'iPhone 13')
