from django.urls import path
from .views import homeview, ContactView, AboutView, BlogView, CarView

app_name = 'core'
urlpatterns = [
    path('', homeview, name="home_page"),
    path('contact/', ContactView.as_view(), name="contact_page"),
    path('about/', AboutView.as_view(), name="about_page"),
    path('blog/', BlogView.as_view(), name="blog_page"),
    path('car/', CarView.as_view(), name="car_page")
]