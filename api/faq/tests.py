
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Faq
from .serializers import FaqSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_faq(title="", content=""):
        if title != "" and content != "":

            Faq.objects.create(title=title, content=content)

    def setUp(self):
        # add test data
        self.create_faq("like glue", "sean paul")
        self.create_faq("simple song", "konshens")
        self.create_faq("love is wicked", "brick and lace")
        self.create_faq("jam rock", "damien marley")

