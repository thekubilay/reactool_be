from django.contrib import admin
from panorama.models import Panorama


@admin.register(Panorama)
class PanoramaAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)
	list_display = ('id', 'name', 'project', 'type', 'day_time', 'image', 'is_loop', 'is_panoramic', 'floor',)
	list_display_links = ('id', 'project', 'image')
	list_filter = ('project',)
	search_fields = ('project__name', 'id',)
	list_per_page = 25

	# make uppercase type before save
	def save_model(self, request, obj, form, change):
		obj.type = obj.type.upper()
		super().save_model(request, obj, form, change)

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name in ('project',):
			kwargs["queryset"] = db_field.related_model.objects.order_by('name')
		return super().formfield_for_foreignkey(db_field, request, **kwargs)
