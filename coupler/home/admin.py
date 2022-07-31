from django.contrib import admin

from .models import Signup
from .models import Detail

# Register your models here.

admin.site.register(Signup)
admin.site.register(Detail)