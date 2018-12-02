from django.apps import AppConfig
from django.db.models.signals import post_migrate
# from django.contrib.auth.models import Group, Permission


def create_group(name, permissions):

    print("group created")
    # [group.permissions.add(permission) for permission in permissions]


def define_groups(sender, **kwargs):
    # permissions = [
    # ]
    # create_group('Administrator', permissions)
    # create_group('Supervisor', permissions)
    # create_group('Instructor',permissions)
    # create_group('TA', permissions)
    print("Defined groups")

class MyAppConfig(AppConfig):
    name = 'TAServer'
    verbose_name = 'TAServer'

    def ready(self):
        post_migrate.connect(define_groups, sender=self)
