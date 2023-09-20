from django.conf.urls.static import static

from travelproject import settings
from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    # path('add/',views.addition,name='addition'),
    # path('contact/',views.contact,name='contact')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)