from django.shortcuts import render
from django.views.decorators.cache import cache_page
from allauth.account.views import SignupView, LoginView


# @cache_page(60 * 5)
def landing_view(request):
    context = {
        "title": "Welcome to Our Landing Page",
        "description": "This is a cached landing page.",
    }
    return render(request, "landing.html", context)

