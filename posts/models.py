from django.db import models

CATEGORY_LIST = (
    ('py', 'python'),
    ('dj', 'django'),
)

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.TextField(choices=CATEGORY_LIST)

    def __str__(self):
        return self.title