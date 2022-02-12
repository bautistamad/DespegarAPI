from distutils.log import error
from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.core.exceptions import PermissionDenied,ValidationError
# from login.models import User


class ProductPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        user_allowed_methods = ['GET','PATCH']
        superuser_allowed_methods = ['POST','GET','PUT','PATCH','DELETE']
        # user = get_user(request)      
        if request.user.is_superuser and request.method in superuser_allowed_methods:
            return True                      
        if not request.user.is_authenticated:
            return False                       
        if request.method in user_allowed_methods:
            return True                    
        raise PermissionDenied()

class PackagePermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        user_allowed_methods = ['GET','PATCH','POST']
        superuser_allowed_methods = ['POST','GET','PUT','PATCH','DELETE']
        if request.user.is_superuser and request.method in superuser_allowed_methods:
            return True
        if not request.user.is_authenticated:
            return False
        if request.method in user_allowed_methods:
            return True
        raise PermissionDenied()

