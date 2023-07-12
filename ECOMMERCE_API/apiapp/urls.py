from django.urls import path
from .views import ListCategory,DetailCategory,ListBook,DetailBook,ListProduct,DetailProduct,ListUser,DetailUser,home


urlpatterns = [
    path('categories/',ListCategory.as_view(),name='category'),
    path('categories/<int:pk>/',DetailCategory.as_view(),name='singlecategorie'),
    path('books',ListBook.as_view(),name='books'),
    path('books/<int:pk>/',DetailBook.as_view(),name='singlebook'),
    path('products',ListProduct.as_view(),name='products'),
    path('products/<int:pk>/',DetailProduct.as_view(),name='singleproduct'),

    path('users/', ListUser.as_view(), name='users'),
    path('users/<int:pk>/', DetailUser.as_view(), name='singleuser'),

]