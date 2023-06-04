from django.contrib import admin
from plans.models import Plan


class PlanAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)
	list_display = ('id', 'name', 'plan_type', 'image')
	list_display_links = ('id', 'image')
	list_filter = ('project',)  # Add project_group to list_filter
	search_fields = ('name', 'plan_type', 'project__name', 'id')
	list_per_page = 25

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name in ('project',):  # Check if it's either company or project_group
			kwargs["queryset"] = db_field.related_model.objects.order_by('name')
		return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Plan, PlanAdmin)
