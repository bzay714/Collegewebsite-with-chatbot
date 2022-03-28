
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('bba/',views.bba,name='bba'),
    path('bit/',views.bit,name='bit'), 
    path('inquiry/',views.inquiry,name='inquiry'),  
    path('info/<str:id>/',views.info,name='info'),  
    path('api/khalti_payment',views.khalti,name='verify_payment'),
    path('receiveMessage/',views.receiveMessage,name="receiveMessage")

]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)