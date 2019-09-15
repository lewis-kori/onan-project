from django.urls import path
from .views import index,accountCreate,updateAccount,deleteAccount

app_name = "accounts"

urlpatterns = [
    path('',index.as_view(),name="index"),
    path('create-account',accountCreate.as_view(),name="create"),
    path('update/<int:pk>',updateAccount.as_view(),name="update"),
    path('delete/<int:pk>',deleteAccount.as_view(),name="delete"),
]
