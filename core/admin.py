from django.contrib import admin
from .models import Service, Position, Employee, Feature


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
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'active', 'modified')

