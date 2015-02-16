from django.contrib import admin
from .models import Accounts


class AccountsAdmin(admin.ModelAdmin):
	pass

admin.site.register(Accounts)
