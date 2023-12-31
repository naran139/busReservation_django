from app import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/',views.login_page, name='login'),
    path('register/',views.register, name='register'),
    path('bus/',views.bus,name="bus"),
    path('logout/',views.logout_page,name="logout"),
    # path('bookings/',views.bookings, name="bookings"),
    path('bookingForm/<schedPk>/',views.bookingForm, name="bookings"),
    path('save_book/<schedPk>/',views.save_book,name="save_book"),
]
