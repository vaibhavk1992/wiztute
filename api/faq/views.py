from rest_framework import generics
from .models import Faq
from .serializers import FaqSerializer
from django.shortcuts import redirect
from django.http import HttpResponse

class ListFaqView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer



def create_faq(title="", content=""):
    if title != "" and content != "":
        Faq.objects.create(title=title, content=content)
        return redirect('something1')

def setUp(self):
    # add test data
    create_faq("like glue111111111111", "vaibhav")
    create_faq("simple song", "konshens")
    create_faq("love is wicked", "brick and lace")
    create_faq("jam rock", "damien marley")
    html = "<html><body>the faq has been created.</body></html>"
    return HttpResponse(html)