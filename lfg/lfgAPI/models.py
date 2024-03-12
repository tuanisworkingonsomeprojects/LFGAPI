from django.db import models

# Create your models here.
class UserData(models.Model):
    username = models.CharField(max_length = 30, null = False, unique= True)
    steamID  = models.CharField(max_length = 17, null = False, unique = True)
    email    = models.CharField(max_length = 100, null = False, unique = True)
    password_hash256 = models.CharField(max_length = 64, null = False, unique = True)
    rating   = models.IntegerField(null = False, default = 0)

class SessionData(models.Model):

    
    session_name = models.CharField(max_length = 20, null = False, unique = True)

     # When a User is deleted his/her session is also deleted
    host_user = models.ForeignKey(UserData, on_delete = models.CASCADE, related_name = "host")

    create_at = models.DateTimeField(auto_now_add = True)
    max_no_player = models.IntegerField(null = False, default = 2)
    participants  = models.ManyToManyField(UserData, 
                                           through = "SessionList", 
                                           through_fields = ("session", "participant"))


class SessionList(models.Model):

    # When the session is deleted the user will no longer in the session
    # When the user is deleted the session will no longer has that user
    session = models.ForeignKey(SessionData, on_delete = models.CASCADE)
    participant  = models.ForeignKey(UserData, on_delete = models.CASCADE)

   





    