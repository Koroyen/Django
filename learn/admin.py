# filepath: c:\Users\Asus\Desktop\beginning\learn\admin.py
from django.contrib import admin
from .models import CustomUser, Hotspot, Event, Post
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('email',)
    search_fields = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active')}
        ),
    )

class HotspotAdmin(admin.ModelAdmin):
    exclude = ('created_by', 'updated_by')  # Hide these fields in the admin form

    def save_model(self, request, obj, form, change):
        if not change or not obj.created_by:
            obj.created_by = request.user  # Set on creation
        obj.updated_by = request.user      # Always set on save
        super().save_model(request, obj, form, change)

class PostAdmin(admin.ModelAdmin):
    exclude = ('author',)  # Hide author in the admin form

    def save_model(self, request, obj, form, change):
        if not change or not obj.author:
            obj.author = request.user  # Set on creation
        super().save_model(request, obj, form, change)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Hotspot, HotspotAdmin)
admin.site.register(Event)
admin.site.register(Post, PostAdmin)