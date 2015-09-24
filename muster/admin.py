from django.contrib import admin
from django.contrib.auth.models import User
from muster.models import Person

class PersonInline(admin.StackedInline):
	model = Person


class UserAdmin(admin.ModelAdmin):
	inlines = [PersonInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
