from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . import form
urlpatterns = [
    path('', views.home, name='home'),
    path('login',views.login,name='login'),
    path('signup',form.signup,name='signup'),
    path('forgotpassword',views.forgotPassword,name='forgot'),
    path('changepassword',views.changePassword,name='changepassword'),
]
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)