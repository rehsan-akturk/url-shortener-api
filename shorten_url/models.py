import random
import string

from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class ShortUrlModel(models.Model):
    ID_LENGTH = 6
    short_url = models.CharField(max_length=ID_LENGTH, blank=False, unique=True)
    url = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'<short url: {self.short_url} url: {self.url}>'

    def increase_short_url_counter(self) -> None:
        """When a user request a original url with the short_url."""
        self.count += 1
        self.save()

    @classmethod
    def generate_short_url(cls) -> str:
        """
        Generate a short url used to shorten the original url
        making sure short url is not in used.
        """

        CHARACTERS = (
                string.ascii_uppercase
                + string.ascii_lowercase
                + string.digits
        )

        while True:
            short_url = ''.join(
                random.choice(CHARACTERS)
                for _ in range(cls.ID_LENGTH)
            )

            try:
                cls.objects.get(short_url=short_url)
            except ObjectDoesNotExist:
                return short_url
