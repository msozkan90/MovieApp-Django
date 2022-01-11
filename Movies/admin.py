from django.contrib import admin
from .models import Category,Film,Actor,Film_rate
# Register your models here.
class ActorAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}
class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
admin.site.register(Category)
admin.site.register(Actor,ActorAdmin)
admin.site.register(Film,FilmAdmin)
admin.site.register(Film_rate)
