from django.db import models
from BLOG.utils import unique_slug_generator
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.text import slugify
from datetime import datetime
from ckeditor.fields import RichTextField

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import random
import string
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length = 50)

    slug = models.SlugField(unique=True,null=False,blank=False)
    entry_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)
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
    no_of_new_category=models.IntegerField(default=0)
    no_of_blog=models.IntegerField(default=0)
    no_of_comments=models.IntegerField(default=0)
    no_of_activities=models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)
    
    # def slug_generator(sender, instance, *args, **kwargs):
    #     if not instance.slug:
    #         instance.slug = unique_slug_generator(instance)

    def save(self, *args, **kwargs):
        slug_txt=f'{self.user}'
        self.slug = unique_slug_generator(self)
        qs_exists = Profile.objects.filter(slug=slug_txt)
        if qs_exists:
            new_slug = "{slug}-{randstr}".format(
                slug=slug_txt,
                randstr=random_string_generator(size=4)
            )
            self.slug = new_slug
        super(Profile, self).save(*args, **kwargs)
    
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


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))