from django.contrib import admin
from projects.models import Company, Project, ProjectGroup

admin.site.register(ProjectGroup)


class ProjectAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)
	list_display = ('id', 'company', 'name')
	list_display_links = ('id', 'name')
	list_filter = ('company', 'groups')  # Add project_group to list_filter
	search_fields = ('name', 'company__name', 'id')
	list_per_page = 25

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name in ('company', 'project_group'):  # Check if it's either company or project_group
			kwargs["queryset"] = db_field.related_model.objects.order_by('name')
		return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Project, ProjectAdmin)
