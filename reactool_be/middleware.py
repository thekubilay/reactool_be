from rest_framework.permissions import BasePermission
from django.http import HttpResponseForbidden


class ApiPermission(BasePermission):
	def has_permission(self, request, view):
		# Add your custom permission logic here
		# Return True if the user has permission, False otherwise
		# You can access the request.user to check the user's permissions
		return request.user.is_authenticated


class PermissionMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):

		if not request.user.is_authenticated:
			return HttpResponseForbidden("You don't have permission to access this resource.")

		response = self.get_response(request)

		return response
