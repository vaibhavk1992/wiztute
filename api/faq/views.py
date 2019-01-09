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
    create_faq("How would I find tutor on the platform?", "All you need to do is to sign in/sign up from the home page. For sign up process, you need to verify your email address. Once you sign in, select the language you want to learn and select the time slot. Provide your contact number(only once) to complete the registration process. Wiztute executive will contact you to understand your learning requirement in specific and we will allot a tutor accordingly.")
    create_faq("How much do tutors charge? How do I pay for it ?", "Tutor charge on hourly basis. They charge as per their qualification and experience.Wiztute does not control the pricing charges by tutors. Once you have a demo with the tutor, you can subscribe the learning session from the tutor by paying as per tutor’s hourly charges. There is a payment tab on dashboard though which you can pay the amount.")
    create_faq("Will I get any certificate?", "No, wiztute tutors do not provide any certificate.")
    create_faq("Are the timings flexible ?", "Yes, the timings are flexible. You can choose to learn at four different time-slots i.e. 8AM-12PM, 12PM-4PM, 4PM-8PM, 8PM-12AM")
    create_faq("How will the learning process happen?","Once you have the demo with the tutor, you can subscribe the learning session as per your requirement. The whole learning will happen on wiztute platform by direct one-to-one interaction with the tutor. Click on “Go Live” tab at the predetermined time to connect to the tutor.")
    create_faq("Is it online learning ?","Yes, the whole learning process will be online.")
    create_faq("What subjects do tutor teach ?","As of now, you can start learning any spoken language that you want. I.e. Japanese, French, Spanish, etc")
    html = "<html><body>the faq has been created.</body></html>"
    return HttpResponse(html)