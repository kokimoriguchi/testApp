from django.test import TestCase

from django.urls import resolve
from django_app.views import top, app_new, app_edit, app_detail


class TopPageTest(TestCase):
    # def test_top_page_returns_200_and_expected_title(self):
    #     response = self.client.get("/")
    #     self.assertContains(response, "Djangoアプリ", status_code=200)

    def test_top_page_uses_expected_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "django_app/top.html")


class CreateAppTest(TestCase):
    def test_should_resolve_app_new(self):
        found = resolve("/app/new/")
        self.assertEqual(app_new, found.func)


class AppDetailTest(TestCase):
    def test_should_resolve_app_detail(self):
        found = resolve("/app/1/")
        self.assertEqual(app_detail, found.func)


class AppEditTest(TestCase):
    def test_should_resolve_app_edit(self):
        found = resolve("/app/1/edit/")
        self.assertEqual(app_edit, found.func)
