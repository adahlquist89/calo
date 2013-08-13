from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from users.models import CaloUser, Profile

class UserCreationForm(forms.ModelForm):
    """Form para crear usuarios."""
    # Ademas de los fields del modelo de calo user se le agregan los campos para las passwords
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CaloUser
        fields = ('email', 'first_name','last_name')

    def clean_password2(self):
        """Chequea que las passwords matcheen."""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        """Hashea la password y la almacena"""
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CaloUser
        fields = ['email', 'password', 'first_name', 'last_name', 'is_active', 'is_admin']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class ProfileInline(admin.TabularInline):
	model = Profile

class CaloUserAdmin(UserAdmin):
    """Representacion de un calouser en la pantalla de admin."""
    form = UserChangeForm
    add_form = UserCreationForm

    #Los campos que se visualizan, filtros y grupos de campos.
    list_display = ('email', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    inlines = [ProfileInline]

# Para registrar el modelo en el admin
admin.site.register(CaloUser, CaloUserAdmin)
# No usamos los permisos que vienen por defecto de Django, los de grupo y eso
admin.site.unregister(Group)