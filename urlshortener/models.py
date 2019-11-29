from django.db import models


class URL(models.Model):
    long_url = models.CharField(
        max_length=250,
        verbose_name="Long URL"
    )
    url_id = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.long_url

    
    def short(self):
        return 'http://myshort.codes/' + self.url_id + '/'
    

    def long(self):
        return self.long_url