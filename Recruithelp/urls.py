from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^',include('homepage.urls'),name='homepage'),
    url(r"^payments/", include("payments.urls")),
    url(r'^admin/', admin.site.urls),
]
