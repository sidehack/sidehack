from django.contrib import admin

from .models import *

admin.site.register(Hacker)
admin.site.register(Organization)
admin.site.register(Hack)
admin.site.register(GithubRepository)
