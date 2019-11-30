from django.db import models

import random, string


class Url(models.Model):
    long_url = models.CharField(
        max_length=250,
        verbose_name="Long URL"
    )
    url_id = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.long_url

    
    def short(self):
        return 'http://myshort.codes/' + self.url_id + '/'.lower()
    

    def long(self):
        return self.long_url

    
    def save(self, *args, **kwargs):
        if self.long_url != '':
            # Generate random characters
            random_chars = self.generate_random_chars()
            num_results = Url.objects.filter(url_id=random_chars).count()
            # If random character is in the db already, generate another one
            if num_results:
                random_chars = self.generate_random_chars()

            self.url_id = random_chars
            super(Url, self).save(*args, **kwargs)

    
    def generate_random_chars(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=7))
