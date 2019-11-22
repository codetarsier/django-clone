from django.contrib import admin

try:
    from django.urls import re_path as path, include
except ImportError:
    from django.conf.urls import url as path, include

app_name = 'sample'

urlpatterns = [
    path('^admin/', admin.site.urls),
]
