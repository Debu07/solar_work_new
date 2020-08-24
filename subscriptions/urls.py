from django.urls import path
from . import views

app_name='membership'

urlpatterns = [
 path('',views.home,name="home"),
 path('checkout/',views.checkout,name="checkout"),


]

#  path('update-transaction/<subscription_id>/',views.updateTransactions,name="update_transaction"),
