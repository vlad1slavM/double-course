from django.contrib import admin
from app.models import User
from app.internal.admin.admin_user import AdminUserAdmin

admin.site.site_title = "Backend course"
admin.site.site_header = "Backend course"
admin.site.register(User)
