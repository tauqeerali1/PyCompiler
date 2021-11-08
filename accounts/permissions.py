from django.conf import settings

from rest_framework.permissions import BasePermission

class Check_API_KEY_Auth(BasePermission):
    def has_permission(self, request, view):
        # API_KEY should be in request headers to authenticate requests
        api_key_secret = request.META.get('242244bc8ee5b254b6c79e180853a12f282983e5')
        return api_key_secret == settings.API_KEY_SECRET