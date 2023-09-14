from django.urls import path

from django_app import views

# ここのURLは各機能を持ったアプリケーションのURLを記述すし、設定の方でincludeで読み込むようにしています。
urlpatterns = [
    path("new/", views.app_new, name="app_new"),
    path("<int:app_id>/", views.app_detail, name="app_detail"),
    path("<int:app_id>/edit/", views.app_edit, name="app_edit"),
]
