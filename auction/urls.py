from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name="home"),
    path('bidnow',views.bidnow,name="bidnow"),
    path('onsale',views.onsale,name="onsale"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('tsandcs',views.tsandcs,name="tsandcs"),
    path('login/', views.login_process,name='login'),
    path('logout/', views.logout_process,name='logout'),
    path('faqs',views.faqs,name="faqs"),
    path('bidders',views.bidders,name="bidders"),
    path('product/<int:id>/',views.product, name="product"),
    path('product/<int:id>/make_bid',views.make_bid, name="make_bid"),
]
