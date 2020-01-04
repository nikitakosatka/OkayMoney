from django.contrib import admin
from django.urls import path, include
from django_registration.backends.one_step.views import RegistrationView
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path(
        "accounts/register/",
        RegistrationView.as_view(success_url="/"),
        name="django_registration_register",
    ),
    path("accounts/", include("django_registration.backends.one_step.urls")),
    path("favicon.ico", RedirectView.as_view(url="static/okaymoneyapp/images/icon.png")),
    path("", include("okaymoneyapp.urls")),
]
