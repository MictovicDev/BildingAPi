from django.contrib import admin
from core.models import *
from .models import Project

# class ProjectAdminForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = '__all__'
from django.contrib import admin


class ItemsInline(admin.TabularInline):  # Use admin.StackedInline for a stacked view
    model = Item
    extra = 1  # Number of empty forms to display

class BidItemsInline(admin.TabularInline):  # Use admin.StackedInline for a stacked view
    model = BidItem
    extra = 2


class SuppliersApplicationAdmin(admin.ModelAdmin):
    inlines = [BidItemsInline]

# class RequestAdmin(admin.ModelAdmin):
#     inlines = [ItemsInline, RequestImageInline]

# class ProjectAdmin(admin.ModelAdmin):
#     inlines = [ProjectImageInline]



admin.site.register(Project)
admin.site.register(RecentProject)
admin.site.register(Store)
admin.site.register(Item)
admin.site.register(Request)
admin.site.register(BidForProject)
# admin.site.register(Hire)
admin.site.register(Reviews)
admin.site.register(Notification)
admin.site.register(SuppliersApplication, SuppliersApplicationAdmin)

