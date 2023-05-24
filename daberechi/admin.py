from django.contrib import admin
from .models import Home, About, Profile,Category,Skill, Portfolio,ContactMessage

admin.site.register(Home)

class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class Aboutadmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillInline,
    ]

admin.site.register(Portfolio)

admin.site.register(ContactMessage)