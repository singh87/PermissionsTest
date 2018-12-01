from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser
from django.db import models

class Course(models.Model):

    class Meta:
        permissions = (("can_create_course", "Can create courses"),
                        ("can_edit_course", "Can edit courses"),
                        ("can_delete_course", "Can delete courses"),
                        ("can_view_course", "Can view courses"))
class Section(models.Model):

    class Meta:
        permissions = (("can_create_section", "Can create sections"),
                        ("can_edit_section", "Can edit sections"),
                        ("can_delete_section", "Can delete sections"),
                        ("can_view_section", "Can view sections"))



class Staff(AbstractUser):
    ROLES = (
        ('T', 'TA'),
        ('I', 'Instructor'),
        ('A', 'Administrator'),
        ('S', 'Supervisor')
    )

    # username = models.CharField(max_length=30, default="")
    # password = models.CharField(max_length=30, default="")
    firstname = models.CharField(max_length=30, default="")
    lastname = models.CharField(max_length=30, default="")
    bio = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=30, default="")
    role = models.CharField(max_length=13, choices=ROLES, default="")
    phonenum = models.CharField(max_length=10, default="")
    address = models.CharField(max_length=30, default="")

    class Meta:
        permissions = (("can_create_user", "Can create users"),
                        ("can_edit_user", "Can edit users"),
                        ("can_edit_self", "Can edit users"),
                        ("can_delete_user", "Can delete users"),
                        ("can_view_user", "Can view users"),
                        ("can_view_private", "Can view private user data"),

                        ("can_email_all", "Can send emails to all users"),
                        
                        ("can_assign_ta", "Can assign TA's"),
                        ("can_assign_ins", "Can assign instructors"),
                        
                        ("can_email_tas", "Can send emails"))

    def __str__(self):
        perm_list = self.user_permissions.all().values_list('codename', flat=True)
        return str(perm_list)


        # return "("+ self.role+")"+" "+ self.first_name + " " + self.last_name + " " + self.email
