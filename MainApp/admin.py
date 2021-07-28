from django.contrib import admin
from .models import BlockInfo


class BlockAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("height",)}


admin.site.register(BlockInfo)
