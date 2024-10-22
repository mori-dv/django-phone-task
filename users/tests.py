from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserRegisterViewTest(TestCase):
    def setUp(self):
        self.user_model = get_user_model()

    def test_register_view(self):
        response = self.client.post(reverse('users:register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user_model.objects.count(), 1)


class UserLoginViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

    def test_login_view(self):
        response = self.client.post(reverse('users:login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue('_auth_user_id' in self.client.session)
