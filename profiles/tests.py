from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
from .models import Profile
from .views import index, profile


class ProfileIndexViewTest(TestCase):
    def setUp(self):
        """setup 2 users and 2 profiles"""
        self.user = User.objects.create_user(username="testuser", password="password")
        self.user2 = User.objects.create_user(
            username="testuser2", password="password2"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")
        self.profile2 = Profile.objects.create(user=self.user2, favorite_city="Londres")

    def test_index_view_status_code(self):
        # Test status code is 200
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template_index_used(self):
        # Test good templates is used (index.html)
        response = self.client.get(reverse("profiles:index"))
        self.assertTemplateUsed(response, "profiles/index.html")

    def test_index_view_context(self):
        # Test context is ok (profiles_list)
        response = self.client.get(reverse("profiles:index"))
        self.assertTrue("profiles_list" in response.context)
        self.assertEqual(len(response.context["profiles_list"]), 2)

    def test_index_view_content(self):
        # test if index content is ok
        response = self.client.get(reverse("profiles:index"))
        self.assertContains(response, "testuser")
        self.assertContains(response, "testuser2")


class ProfilesProfileViewTest(TestCase):
    def setUp(self):
        """setup user and profile"""
        self.user = User.objects.create_user(username="testuser", password="password")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_profile_view_status_code(self):
        # Test if the status code is ok(200)
        url = reverse("profiles:profile", args=[self.profile.user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_profile_view_templates_index_used(self):
        # Test if the good templates is used for the index view
        url = reverse("profiles:profile", args=[self.profile.user.username])
        response = self.client.get(url)
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_letting_view_context(self):
        # Test if context is good (lettings_list is the context)
        url = reverse("profiles:profile", args=[self.profile.user.username])
        response = self.client.get(url)
        self.assertEqual(response.context["profile"], self.profile)

    def test_letting_view_content(self):
        # Test if content titles are good
        url = reverse("profiles:profile", args=[self.profile.user.username])
        response = self.client.get(url)
        self.assertContains(response, "testuser")
        self.assertContains(response, "Paris")


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_profile_creation(self):
        """Test that a Profile object is correctly created"""
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.favorite_city, "Paris")

    def test_profile_str(self):
        """Test the string representation of the Profile object"""
        self.assertEqual(str(self.profile), "testuser")


class URLTest(TestCase):

    def test_url_resolve(self):
        # Verify 'profiles:index' resolve the good view
        url = reverse("profiles:index")
        self.assertEqual(resolve(url).func, index)

    def test_letting_url_resolves(self):
        # Verify url 'profiles:profile' and id resolve the good view
        url = reverse("profiles:profile", args=[1])
        self.assertEqual(resolve(url).func, profile)

    def test_index_url_status_code(self):
        # Verify url 'profiles:index' status code is 200
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)
