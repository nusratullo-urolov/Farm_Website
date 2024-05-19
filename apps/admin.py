from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Combine, Tractor, MineralEndorsements, Workers, OtherEquipments


@admin.register(Combine)
class CombineAdmin(ModelAdmin):
    pass

@admin.register(Tractor)
class TractorAdmin(ModelAdmin):
    pass

@admin.register(MineralEndorsements)
class MineralEndorsementsAdmin(ModelAdmin):
    pass

@admin.register(Workers)
class WorkersAdmin(ModelAdmin):
    pass

@admin.register(OtherEquipments)
class OtherEquipmentsAdmin(ModelAdmin):
    pass
