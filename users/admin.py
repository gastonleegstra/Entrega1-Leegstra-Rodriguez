from django.contrib import admin

# Register your models here.
from users.models import User_profile

admin.site.register(User_profile)