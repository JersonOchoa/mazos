from django.contrib import admin
from mazos.models import Tropa, TropaAdmin, Arena, ArenaAdmin

admin.site.register(Tropa, TropaAdmin)
admin.site.register(Arena, ArenaAdmin)
