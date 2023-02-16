from django.contrib import admin

from .models import Signup
from .models import Detail
from .models import Detaila
from .models import Preference1
from .models import Preference2
from .models import Blog
from .models import Post
from .models import Social




# Register your models here.

admin.site.register(Signup)
admin.site.register(Detail)
admin.site.register(Detaila)
admin.site.register(Preference1)
admin.site.register(Preference2)
admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Social)
