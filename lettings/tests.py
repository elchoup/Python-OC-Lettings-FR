from django.test import TestCase
from django.urls import reverse, resolve
from django.db.utils import IntegrityError
from .models import Letting, Address
from .views import index, letting


class LettingsIndexViewsTest(TestCase):
    def setUp(self):
        """Create objects adress and letting for tests"""
        self.address1 = Address.objects.create(
            number=15,
            street="Main Street",
            city="Albany",
            state="New York",
            zip_code=12201,
            country_iso_code=3166,
        )

        self.address2 = Address.objects.create(
            number=5,
            street="Quai de Montebello",
            city="Paris",
            state="Ile de France",
            zip_code=75005,
            country_iso_code=3166,
        )

        Letting.objects.create(title="Cozy Cottage", address=self.address1)
        Letting.objects.create(title="Amazing Loft", address=self.address2)

    def test_index_view_status_code(self):
        # Test if the status code is ok(200)
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_templates_index_used(self):
        # Test if the good templates is used for the index view
        response = self.client.get(reverse("lettings:index"))
        self.assertTemplateUsed(response, "lettings/index.html")

    def test_index_view_context(self):
        # Test if context is good (lettings_list is the context)
        response = self.client.get(reverse("lettings:index"))
        self.assertTrue("lettings_list" in response.context)
        self.assertEqual(len(response.context["lettings_list"]), 2)

    def test_index_view_content(self):
        # Test if content titles are good
        response = self.client.get(reverse("lettings:index"))
        self.assertContains(response, "Cozy Cottage")
        self.assertContains(response, "Amazing Loft")

    def test_adress_not_unique(self):
        # Test error if adress is not unique
        with self.assertRaises(IntegrityError):
            Letting.objects.create(title="Not unique", address=self.address1)


class LettingsLettingViewsTest(TestCase):
    def setUp(self):
        """Create objects adress and letting for tests"""
        self.address = Address.objects.create(
            number=5,
            street="Quai de Montebello",
            city="Paris",
            state="Ile de France",
            zip_code=75005,
            country_iso_code=3166,
        )

        self.letting = Letting.objects.create(
            title="Amazing Loft", address=self.address
        )

    def test_letting_view_status_code(self):
        # Test if the status code is ok(200)
        url = reverse("lettings:letting", args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_letting_view_templates_index_used(self):
        # Test if the good templates is used for the index view
        url = reverse("lettings:letting", args=[self.letting.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response, "lettings/letting.html")

    def test_letting_view_context(self):
        # Test if context is good (lettings_list is the context)
        url = reverse("lettings:letting", args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.context["title"], self.letting.title)
        self.assertEqual(response.context["address"], self.letting.address)

    def test_letting_view_content(self):
        # Test if content titles are good
        url = reverse("lettings:letting", args=[self.letting.id])
        response = self.client.get(url)
        self.assertContains(response, "Amazing Loft")
        self.assertContains(response, "5 Quai de Montebello")


class AddressModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=1,
            street="Rue Lebrun",
            city="Paris",
            state="IDF",
            zip_code="75",
            country_iso_code="3166",
        )

    def test_address_creation(self):
        """Test that an Address object is correctly created"""
        self.assertEqual(self.address.number, 1)
        self.assertEqual(self.address.street, "Rue Lebrun")
        self.assertEqual(self.address.city, "Paris")
        self.assertEqual(self.address.state, "IDF")
        self.assertEqual(self.address.zip_code, "75")
        self.assertEqual(self.address.country_iso_code, "3166")

    def test_address_str(self):
        """Test the string representation of the Address object"""
        self.assertEqual(str(self.address), "1 Rue Lebrun")


class LettingModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=5,
            street="Quai de Montebello",
            city="Paris",
            state="Ile de France",
            zip_code=75005,
            country_iso_code=3166,
        )
        self.letting = Letting.objects.create(
            title="Amazing Loft", address=self.address
        )

    def test_letting_creation(self):
        """Test that a Letting object is correctly created"""
        self.assertEqual(self.letting.title, "Amazing Loft")
        self.assertEqual(self.letting.address, self.address)

    def test_letting_str(self):
        """Test the string representation of the Letting object"""
        self.assertEqual(str(self.letting), "Amazing Loft")


class URLTest(TestCase):

    def test_url_resolve(self):
        # Verify 'lettings:index' resolve the good view
        url = reverse("lettings:index")
        self.assertEqual(resolve(url).func, index)

    def test_letting_url_resolves(self):
        # Verify url lettings:letting and id resoleve the good view
        url = reverse("lettings:letting", args=[1])
        self.assertEqual(resolve(url).func, letting)

    def test_index_url_status_code(self):
        # Verify url lettings:letting status code is 200
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)
