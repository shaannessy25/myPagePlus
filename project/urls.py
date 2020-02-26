from django.urls import path, include
from project.views import Home, myPagePlus
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Home.as_view(), name='home-page'),
    path('my_page_plus/', myPagePlus.as_view(), name='my-page'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
