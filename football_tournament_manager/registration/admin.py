from django.contrib import admin
from .models import Team, Player, Coach, Manager, Fixture


admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Coach)
admin.site.register(Manager)
admin.site.register(Fixture)