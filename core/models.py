from django.db import models
from django.contrib.auth.models import AbstractUser


def get_file_name_ext(file_path):
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, fileName):
    _, ext = get_file_name_ext(fileName)
    final_name = f'{instance.id}-{instance.username}.{ext}'
    return f'avatars/{final_name}'


class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return str(self.id)

class Contact(models.Model):
    full_name = models.CharField(max_length=64)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    body = models.TextField()
    response = models.TextField(null=True, blank=True)
    is_responsed = models.BooleanField(default=False, help_text='if this field is checked means that the respons has send to email address.')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.full_name)
    