from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# user =User.objects.filter('nisarg').first()
#user.profile
#user.profile.image
# the onetoone relationship means one user have only one profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no=models.TextField(max_length=10,default="")
    clg_name=models.TextField(max_length=400,default="")
    degree=models.TextField(max_length=400,default="")
    skill=models.TextField(max_length=1200,default="")
    jobs=models.TextField(max_length=500,default="")
    image = models.ImageField(default='default.jpg', upload_to='blog/profile_pics')
    friends=models.TextField(max_length=5000,default="")

    def __str__(self):
        return f'{self.user.username} Profile'

    #def save(self):
    # super().save()
    # img=Image.open(self.image.path)
    # if img.height>300 or img.width>300:
    # #         output_size=(300,300)
    # #         img.thumbnail(output_size)
    # #         img.save(self.image.path)