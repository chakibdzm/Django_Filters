from django.urls import path,include
from . import views
urlpatterns=[
    path('product/',views.ProductList.as_view() ),
    path('product/<int:id>/',views.ProductDetail.as_view())
]