from django.contrib import admin
from links.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)
	list_display = ('id', 'url', 'name', 'project', 'image')
	list_display_links = ('id', 'url', 'name', 'project', 'image')
	list_filter = ('project',)
	search_fields = ('project__name', 'id', 'url')
	list_per_page = 25

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name in ('project',):  # Check if it's either company or project_group
			kwargs["queryset"] = db_field.related_model.objects.order_by('name')
		return super().formfield_for_foreignkey(db_field, request, **kwargs)
