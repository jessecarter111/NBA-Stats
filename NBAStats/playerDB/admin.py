from django.contrib import admin

from .models import Player, Team

# Register your models here.

class PlayerInline(admin.TabularInline):
    model = Player

class TeamAdmin(admin.ModelAdmin):
    model = Team
    inlines = [
        PlayerInline,
    ]

admin.site.register(Team, TeamAdmin)
admin.site.register(Player)