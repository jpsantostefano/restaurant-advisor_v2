from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Post, Comment, Profile

#Unregister Groups
admin.site.unregister(Group)

# Mix Profile info into User info
class ProfileInline(admin.StackedInline):
    model = Profile

#Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    #Just display username fields on admin page
    fields = ['username']
    inlines = [ProfileInline]

# Unregister initial User
admin.site.unregister(User)

# Registerer User and Profile
admin.site.register(User, UserAdmin)

admin.site.register(Post)
admin.site.register(Comment)

# admin.site.register(Profile)