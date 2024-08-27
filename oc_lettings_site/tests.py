from django.test import TestCase
from django.urls import reverse, resolve


class OcLettingViewTests(TestCase):

    def test_index_view_status_code(self):
        """Test if the index view returns a 200 status code"""
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template_used(self):
        """Test if the index view uses the correct template"""
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")

    def test_trigger_error_view(self):
        """Test if the trigger_error view raises a 500 error"""
        with self.assertRaises(ZeroDivisionError):
            self.client.get(reverse("trigger_error"))


def test_dummy():
    assert 1
