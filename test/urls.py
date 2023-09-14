"""
URL configuration for test project.

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
from django.urls import path, include  # includeを追加

from django_app.views import top

# pathは第一引数にURLのパターン、第二引数にview関数、第三引数にURLの名前を受け取る。
urlpatterns = [
    path("", top, name="top"),
    path(
        "app/", include("django_app.urls")
    ),  # includeを追加することで、django_app/urls.pyのURLを読み込むことができる。
    path("accounts/", include("accounts.urls")),  # accounts/urls.pyを読み込む。
    path("admin/", admin.site.urls),
]
