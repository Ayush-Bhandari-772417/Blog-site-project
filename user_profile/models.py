from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.text import slugify
from datetime import datetime
from ckeditor.fields import RichTextField

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)

    slug = models.SlugField()
    entry_date = models.DateTimeField(auto_now_add=True, null=True)
    undated_date = models.DateTimeField(auto_now=True, null=True)

    photo = models.ImageField(upload_to='images/profile_photo', default='Capture.PNG')
    image_thumbnail =ImageSpecField(source='photo', processors=[ResizeToFill(100,50)], format='JPEG', options={'quality': 60})
    tag = RichTextField(blank=True,null=True)
    contact = models.CharField(max_length=10, null=True)
    email = models.EmailField(null=True, max_length = 50,help_text='Enter your email addresses')
    address = models.CharField(max_length = 50,blank=True,null=True)
    about = RichTextField(blank=True,null=True)
    Hobby = RichTextField(blank=True,null=True)
    Education = RichTextField(blank=True,null=True)
    Licenses_certifications = RichTextField(blank=True,null=True)
    Volunteering = RichTextField(blank=True,null=True)
    Skills = RichTextField(blank=True,null=True,help_text='Enter a brief description of your skills')
    Honors_awards = RichTextField(blank=True,null=True)
    Languages = RichTextField(blank=True,null=True)
    Organizations = RichTextField(blank=True,null=True)

    def __str__(self):
        return str(self.user)
    
    # def create_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(sender=instance)
    #         print("Profile created")
    
    # post_save.connect(create_profile, sender=User)

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save(self, *args, **kwargs):
        slug_txt=f'{self.user}'
        self.slug = slugify(slug_txt)
        super(Profile, self).save(*args, **kwargs)