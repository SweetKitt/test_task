from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType
from objectpack.ui import ModelEditWindow
from objectpack.actions import ObjectPack
from .ui import UserAddWindow, ActionPackFormWithContentTypeField


class PermissionActionPack(ObjectPack):
    model = Permission
    add_to_desktop = True
    can_delete = True
    content_type_field = 'content_type'


    def _get_field_for_content_type(self):
         return Permission._meta.get_field('content_type')

    def get_ui_form(self):
         return ActionPackFormWithContentTypeField


class GroupActionPack(ObjectPack):
    model = Group
    add_to_desktop = True
    can_delete = True
    add_window = edit_window = ModelEditWindow.fabricate(model=Group)


class ContentTypeActionPack(ObjectPack):
    model = ContentType
    add_to_desktop = True
    can_delete = True
    add_window = edit_window = ModelEditWindow.fabricate(model=ContentType)


class UserActionPack(ObjectPack):
    model = User
    add_to_desktop = True
    can_delete = True
    add_window = edit_window = UserAddWindow
