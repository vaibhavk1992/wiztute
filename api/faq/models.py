from django.db import models


class Faq(models.Model):
    # faq title
    title = models.CharField(max_length=255, null=False)
    # Answer
    content = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.content)