from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    path('search/',views.searching,name='search'),
    path('<slug:c_slug>/<slug:product_slug>',views.productdetail,name='details'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),


]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)