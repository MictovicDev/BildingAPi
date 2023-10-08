from django.contrib import admin
from core.models import *
from .models import Project

# class ProjectAdminForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = '__all__'
from django.contrib import admin


# class ProjectImageInline(admin.TabularInline):  # Use admin.StackedInline for a stacked view
#     model = ProjectImage
#     extra = 1  # Number of empty forms to display

# class ProjectAdmin(admin.ModelAdmin):
#     inlines = [ProjectImageInline]

class RequestImageInline(admin.TabularInline):  # Use admin.StackedInline for a stacked view
    model = RequestImage
    extra = 1  # Number of empty forms to display


class ProjectImageInline(admin.TabularInline):  # Use admin.StackedInline for a stacked view
    model = ProjectImage
    extra = 1 

class ItemsInline(admin.TabularInline):  # Use admin.StackedInline for a stacked view
    model = Item
    extra = 1  # Number of empty forms to display


# class SuppliersApplicationAdmin(admin.ModelAdmin):
#     inlines = [RequestImageInline]

class RequestAdmin(admin.ModelAdmin):
    inlines = [ItemsInline, RequestImageInline]

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]



admin.site.register(Project,ProjectAdmin)
admin.site.register(RecentProject)
admin.site.register(Store)
# admin.site.register(SuppliersApplication, SuppliersApplicationAdmin)
admin.site.register(Item)
admin.site.register(Request, RequestAdmin)
admin.site.register(BidForProject)
# admin.site.register(ProjectImage)
