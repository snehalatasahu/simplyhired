from django.contrib import admin

from .models import Company, Internship


# class InternshipInline(admin.TabularInline):
#     model = Internship

# class CompanyAdmin(admin.ModelAdmin):
#     model = Company
#     inlines = [InternshipInline]


# admin.site.register(Company, CompanyAdmin)
# admin.site.register(Internship)
admin.site.register(Company)
admin.site.register(Internship)
