from django.contrib import admin

# Register your models here.

from catalog.models import Evi_type, Evidence, Evi_case

admin.site.register(Evi_type)
admin.site.register(Evidence)
admin.site.register(Evi_case)


