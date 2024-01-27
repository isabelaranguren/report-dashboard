from django.contrib import admin
from .models import Client, Keyword, Report, SearchEngineListing, SERPPosition

admin.site.register(Client)
admin.site.register(Keyword)
admin.site.register(Report)
admin.site.register(SearchEngineListing)
admin.site.register(SERPPosition)

