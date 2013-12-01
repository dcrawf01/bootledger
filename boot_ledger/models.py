from django.db import models
from django.contrib import admin

class Item(models.Model):
	distributor = models.CharField(max_length=60)
	category = models.CharField(max_length=60)
	sub_category = models.CharField(max_length=60)
	name = models.CharField(max_length=60)
	year = models.CharField(max_length=20)
	country = models.CharField(max_length=60)
	region = models.CharField(max_length=60)

	def __str__(self):

		return '  '.join([
			self.distributor,
			self.category,
			self.sub_category,
			self.name,
			self.year,
			self.country,
			self.region,
		])

class ItemAdmin(admin.ModelAdmin):
    list_display = ["distributor", "category", "sub_category", "country", "region", "name", "year"]
    search_fields = ["distributor", "category"]

admin.site.register(Item, ItemAdmin)

# Create your models here.
