from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.text import slugify
from datetime import datetime
from ckeditor.fields import RichTextField

from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    adder = models.OneToOneField(User, null=True, on_delete=models.CASCADE, editable=False)
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    title = models.CharField(max_length = 100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    slug = models.SlugField(unique=True,null=False,blank=False,editable=False)
    written_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    main_picture = models.ImageField(upload_to='images/user_blog_photo', default='Capture.PNG')
    image_thumbnail =ImageSpecField(source='main_picture', processors=[ResizeToFill(100,50)], format='JPEG', options={'quality': 60})
    Content = RichTextField(blank=False,null=False)
    view = models.IntegerField(default=0)
    count_comments=models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        slug_txt=str(datetime.now())+''+self.title
        self.slug_title = slugify(slug_txt)
        super(BlogPost, self).save(*args, **kwargs)

class BlogComment(models.Model):
    comment=RichTextField(blank=False,null=False)
    commentor=models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    date_commented=models.DateTimeField(auto_now_add=True)
    blog=models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name="comments")

    def __str__(self):
        return self.comment
