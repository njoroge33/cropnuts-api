from django.db import models

class User(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=60)
    # password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    def __str__(self):
        return self.username