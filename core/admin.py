from django.contrib import admin
from .models import Service, Position, Employee, Feature, Plan, Client


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('position', 'active', 'modified')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'icon', 'active', 'modified')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'active', 'modified')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'active', 'modified')


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'modified')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'occupation', 'rating', 'active', 'modified')

