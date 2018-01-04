from typing import Callable
def refine_get_urls(original: Callable) -> Callable:
    def get_urls():
        from django.contrib import admin
        from .admin_urls import get_admin_urls
        admin.autodiscover()
        return original() + get_admin_urls()
    return get_urls
