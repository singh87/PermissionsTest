# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.management import create_permissions
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


PERMISSIONS_Admin = [
        'can_create_course','can_edit_course','can_delete_course','can_view_course',
        'can_create_section','can_edit_section','can_delete_section','can_view_section','can_create_user','can_edit_user','can_edit_self',
        'can_delete_user','can_view_user','can_view_private','can_email_all'
]
PERMISSIONS_Supervisor = [
        'can_create_course','can_edit_course','can_delete_course','can_view_course',
        'can_create_section','can_edit_section','can_delete_section','can_view_section','can_create_user','can_edit_user','can_edit_self',
        'can_delete_user','can_view_user','can_view_private','can_email_all','can_assign_ta','can_assign_ins'
]
PERMISSIONS_Instructor = [
        'can_view_course','can_edit_self','can_view_user','can_view_private','can_assign_ta','can_email_tas'
]
PERMISSIONS_TA = [
        'can_view_course','can_view_section','can_edit_self','can_view_user'
]


def create_group(apps, schema_editor):

    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None



    group, created = Group.objects.get_or_create(name='Administrator')   
    if created:
        permissions = [Permission.objects.get(codename=i) for i in PERMISSIONS_Admin]
        group.permissions.add(*permissions)
                        
        print('Admin Group created')

    #Supervisor
    group, created = Group.objects.get_or_create(name='Supervisor') 
    if created:
        permissions = [Permission.objects.get(codename=i) for i in PERMISSIONS_Supervisor]
        group.permissions.add(*permissions)
        print('Supervisor Group created')

    #Instructor
    group, created = Group.objects.get_or_create(name='Instructor') 
    if created:
        permissions = [Permission.objects.get(codename=i) for i in PERMISSIONS_Instructor]
        group.permissions.add(*permissions)
        print('Instructor Group created')

    #TA
    group, created = Group.objects.get_or_create(name='TA') 
    if created:
        permissions = [Permission.objects.get(codename=i) for i in PERMISSIONS_TA]
        group.permissions.add(*permissions)
        print('TA Group created')    
    


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('TAServer', '0001_initial'),
        

    ]

    operations = [
        migrations.RunPython(create_group),
    ]
