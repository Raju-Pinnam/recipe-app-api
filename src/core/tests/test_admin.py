from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            email='superuser@gmail.com',
            username='superuser',
            password='superuser',
        )
        self.client.force_login(self.admin_user)
        self.user = User.objects.create_user(
            email='normaluser@gmail.com',
            username='normaluser',
            password='normaluser'
        )

    def test_users_listed(self):
        """Test users are listed in user admin page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.username)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test user edit page"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/1/
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test create user page in admin"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
