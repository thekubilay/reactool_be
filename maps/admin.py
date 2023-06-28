import requests
import json

from django.conf import settings
from django.contrib import admin
from django import forms
from maps.models import Map, MapCategory, MapImage


def get_lat_lng(address):
	url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={settings.GOOGLE_MAP_API_KEY}"
	response = requests.get(url)
	data = json.loads(response.text)
	lat = data['results'][0]['geometry']['location']['lat']
	lng = data['results'][0]['geometry']['location']['lng']
	return lat, lng


class MapAdminForm(forms.ModelForm):
	class Meta:
		model = Map
		fields = '__all__'
		widgets = {
			'category': forms.Select,
		}


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)
	list_display = ('id', 'name', 'address', 'category', 'type', 'icon_name', 'icon_size', 'url', )
	list_display_links = ('id',)
	list_filter = ('project',)
	search_fields = ('project__name', 'name', 'address', 'category')
	list_per_page = 25

	def formfield_for_dbfield(self, db_field, request, **kwargs):
		if db_field.name == 'category':
			kwargs['queryset'] = MapCategory.objects.all()
		return super().formfield_for_dbfield(db_field, request, **kwargs)

	def save_model(self, request, obj, form, change):
		if obj.lat is None and obj.lng is None:
			lat, lng = get_lat_lng(obj.address)
			obj.lat = lat
			obj.lng = lng

		obj.save()

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name in ('project',):
			kwargs["queryset"] = db_field.related_model.objects.order_by('name')
		return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(MapCategory)
class MapCategoryAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)
	list_display = ('id', 'name',)
	list_display_links = ('id',)
	search_fields = ('name',)
	list_per_page = 25


@admin.register(MapImage)
class MapImageAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)
	list_display = ('id', 'map', 'image',)
	list_display_links = ('id',)
	search_fields = ('map__name', 'image',)
	list_filter = ('map',)
	list_per_page = 25

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name in ('map',):
			kwargs["queryset"] = db_field.related_model.objects.order_by('name')
		return super().formfield_for_foreignkey(db_field, request, **kwargs)
