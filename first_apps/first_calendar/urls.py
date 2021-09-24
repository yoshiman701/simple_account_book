"""first_apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .import views

app_name = "first_calendar"
urlpatterns = [

    path('', views.OneMonthView.as_view(), name='month'),
    
    path('month/<int:year>/<int:month>/', views.OneMonthView.as_view(), name='month'),
    
    path('detail/<int:year>/<int:month>/<int:day>/', views.DetailWeekView.as_view(), name='detail'),
    
    path('detail/<int:year>/<int:month>/<int:day>/plot', views.get_svg(), name='plot'),
    
    path('category', views.CategoryView.as_view(), name="category"),

]
