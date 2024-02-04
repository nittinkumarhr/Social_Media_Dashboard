from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from auth_app.form import UserForm,CustomUserChangeForm

# Register your models here.
# Model Admin

# Register your models here.
# Model Admin for custom User model

class CustomUserAdmin(UserAdmin):
   # Form used for adding a new user
   add_form = UserForm
   # Form used for updating user information
   form = CustomUserChangeForm
   
   # The model that this CustomUserAdmin is for
   model = User
   
   # Fieldsets displayed when adding a new user
   add_fieldsets = (
       # First fieldset with title 'Personal Info' and fields 'email', 'full_name', 'username', 'password1', 'password2'
       ('Personal Info', {'fields': ('email', 'full_name', 'username','password1','password2','picture')}),
       # Second fieldset with title 'Permissions' and fields 'is_staff' and 'is_active'
       ('Permissions', {'fields': ('is_staff', 'is_active')}),
       # Add any additional custom fields here
       ('Optional', {'fields': ('bio', 'website','')}),
   )
   
   # Fieldsets displayed when viewing or editing a user
   fieldsets = (
       # First fieldset with title 'Personal Info' and fields 'email', 'full_name', 'username'
       ('Personal Info', {'fields': ('email', 'full_name', 'username','picture')}),
       ('Optional', {'fields': ('bio', 'website')}),
       # Add any additional fieldsets here
   )
admin.site.register(User,CustomUserAdmin)
    
    

