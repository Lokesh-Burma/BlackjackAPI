from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','coins')

class GameAdmin(admin.ModelAdmin):
    list_display = ('game_id','playersCount')


admin.site.register(User, UserAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Hand)