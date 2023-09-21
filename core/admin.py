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


class SuppliersApplicationAdmin(admin.ModelAdmin):
    inlines = [RequestImageInline]

admin.site.register(Project)



# admin.site.register(Project)
admin.site.register(Store)
admin.site.register(Request)
admin.site.register(SuppliersApplication, SuppliersApplicationAdmin)
admin.site.register(Item)
admin.site.register(BidForProject)
# admin.site.register(ProjectImage)
admin.site.register(RequestImage)