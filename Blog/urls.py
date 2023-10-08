"""
URL configuration for Blog01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from Blog import settings


# from posts.views import main_view, posts_view, hashtags_view, post_detail_view, post_create_view
from product.views import main_view, products_view, categories_view, products_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),

    path('products/', products_view),
    path('categories/', categories_view),
    path('products/<int:id>/', products_detail_view),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)