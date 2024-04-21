from django.contrib import admin

from .models import To_do_list
from .models import Done_list


admin.site.register(To_do_list)
admin.site.register(Done_list)

