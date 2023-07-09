from django.contrib import admin
from galleries.models import Gallery


class GalleryAdmin(admin.ModelAdmin):
	readonly_fields = ("id", "thumbnail",)
	list_display = ('id', 'project', 'name', 'file')
	list_display_links = ('id', 'name', 'project', 'file')
	list_filter = ('project',)  # Add project_group to list_filter
	search_fields = ('name', 'project__name', 'id')
	list_per_page = 25

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name in ('project',):
			kwargs["queryset"] = db_field.related_model.objects.order_by('name')
		return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Gallery, GalleryAdmin)
