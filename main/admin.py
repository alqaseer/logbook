from django.contrib import admin
from main.models import Case, Update, CustomUser
# Register your models here.

admin.site.register(Case)
admin.site.register(Update)
admin.site.register(CustomUser)
