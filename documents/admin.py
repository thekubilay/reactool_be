from django.contrib import admin
from documents.models import Document
from django.utils.html import format_html


class DocumentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'file', 'folder_name' 'thumbnail_tag',)
	readonly_fields = ('id',)
	list_display_links = ('id',)

	def thumbnail_tag(self, obj):
		if obj.thumbnail:
			return format_html('<img src="{}" width="150" height="150" />', obj.thumbnail.url)
		else:
			return 'No Thumbnail'

	thumbnail_tag.short_description = 'Thumbnail'


admin.site.register(Document, DocumentAdmin)
