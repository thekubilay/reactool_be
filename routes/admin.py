from django.contrib import admin
from routes.models import Route


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)
	list_display = ('id', 'route_name', 'component_name', 'endpoint', 'front_url_name')
	list_display_links = ('id', 'route_name', 'component_name', 'endpoint', 'front_url_name')
	list_filter = ('project',)
	search_fields = ('project__name', 'route_name', 'component_name', 'endpoint', 'front_url_name')
	list_per_page = 25
