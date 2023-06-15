from django.contrib import admin
from plans.models import RoomPlan, GeneralPlan


@admin.register(RoomPlan)
class PlanAdmin(admin.ModelAdmin):
	readonly_fields = ('id', 'thumbnail')
	list_display = ('id', 'type', 'menu', 'madori', 'alcove', 'terrace', 'image')
	list_display_links = ('id', 'image')
	list_filter = ('project',)
	search_fields = ('project__name', 'id', 'type', 'menu', 'madori')
	list_per_page = 25

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name in ('project',):
			kwargs["queryset"] = db_field.related_model.objects.order_by('name')
		return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(GeneralPlan)
class PlanAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)
	list_display = ('id', 'name', 'image')
	list_display_links = ('id', 'image')
	list_filter = ('project',)
	list_per_page = 25

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name in ('project',):
			kwargs["queryset"] = db_field.related_model.objects.order_by('name')
		return super().formfield_for_foreignkey(db_field, request, **kwargs)
