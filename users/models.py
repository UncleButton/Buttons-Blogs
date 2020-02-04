from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # get image from user
        img = Image.open(self.image.path)

        #set final size and crop size (smallest of height or width)
        desired_size = 300
        crop_size = min(img.width,img.height)

        ratio = (desired_size/crop_size)
        size = (desired_size, desired_size)

        if img.height > desired_size or img.width > desired_size:
            # Crop the center of the image
            img = img.crop(((img.width/2)-(crop_size/2), (img.height/2)-(crop_size/2), (img.width/2)+(crop_size/2), (img.height/2)+(crop_size/2)))   
            
            img.thumbnail(size, Image.ANTIALIAS)

            # resize cropped image to be desired size
            img = img.resize(size)
            
            # save the newly cropped and resized image
            img.save(self.image.path)
