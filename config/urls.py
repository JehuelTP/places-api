"""
URL configuration for config project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

api_prefix = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts
    path(f'{api_prefix}/', include('accounts.urls')),

    # Articles
    path(f'{api_prefix}/', include('articles.urls')),

    # Comments
    path(f'{api_prefix}/', include('comments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )