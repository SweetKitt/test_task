from django import forms
from django.contrib.contenttypes.models import ContentType
from django.forms.widgets import Select
from objectpack.ui import BaseEditWindow
from m3_ext.ui import all_components as ext


class UserAddWindow(BaseEditWindow):
    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label=u'password',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__last_login = ext.ExtDateField(
            label=u'last login',
            name='last_login',
            allow_blank=False,
            anchor='100%',
            format='d.m.Y')

        self.field__superuser_status = ext.ExtCheckBox(
            label=u'superuser status',
            name='is_superuser',
            anchor='100%')

        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__first_name = ext.ExtStringField(
            label=u'first name',
            name='first_name',
            allow_blank=False,
            anchor='100%')

        self.field__last_name = ext.ExtStringField(
            label=u'last name',
            name='last_name',
            allow_blank=False,
            anchor='100%')

        self.field__email_address = ext.ExtStringField(
            label=u'email address',
            name='email',
            allow_blank=False,
            anchor='100%')

        self.field__staff_status = ext.ExtCheckBox(
            label=u'staff status',
            name='is_staff',
            anchor='100%')

        self.field__active = ext.ExtCheckBox(
            label=u'active',
            name='is_active',
            anchor='100%')

        self.field__date_joined = ext.ExtDateField(
            label=u'date joined',
            name='date_joined',
            allow_blank=False,
            anchor='100%',
            format='d.m.Y')

    def _do_layout(self):
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__superuser_status,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email_address,
            self.field__staff_status,
            self.field__active,
            self.field__date_joined
        ))

    def set_params(self, params):
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'


class ActionPackFormWithContentTypeField():
    def get_form_fields(self):
        fields = super(ActionPackFormWithContentTypeField, self).get_form_fields()
        fields['content_type'] = forms.ModelChoiceField(
            queryset=ContentType.objects.all(),
            widget=Select(attrs={'class': 'select'}),
            empty_label=None,
            required=True
        )
        return fields

