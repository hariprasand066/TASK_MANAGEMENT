from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Admin'

class IsKeyManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'KeyManager'

class IsTeamLead(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'TeamLead'

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Manager'

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Employee'
