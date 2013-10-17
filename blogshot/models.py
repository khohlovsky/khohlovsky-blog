# coding:utf-8

from django.db import models
from autoslug import AutoSlugField
from pytils.translit import slugify
from comments.models import Comment
import datetime
from django import forms

class Tag (models.Model):
  slug=AutoSlugField()
  title=models.CharField(verbose_name=u'Тэг',max_length=20)
  description=models.CharField(verbose_name=u'Описание',max_length=100,blank='True')

  def save(self,*args,**kwargs):
    self.slug=slugify(self.title)
    super(Tag, self).save(*args, **kwargs)
  
  def __unicode__(self):
    return self.title
    
  def get_url(self):
    return '/tag/%s/' % self.slug

  class Meta:
    ordering=['slug']

class Category (models.Model):
  slug=AutoSlugField(unique=True)
  image=models.ImageField(verbose_name=u'Изображение', upload_to='cat_images', blank='True')
  title=models.CharField(verbose_name=u'Категория',max_length=20)
  description=models.CharField(verbose_name=u'Описание',max_length=100,blank='True')
      
  def save(self,*args,**kwargs):
     self.slug=slugify(self.title)
     super(Category,self).save(*args, **kwargs)	  
  def __unicode__(self):
     return self.title
  def get_url(self):
     return '/category/%s/' % self.slug
		
  class Meta:
     ordering=['slug']

class Post (models.Model):
  slug=AutoSlugField(unique=True,max_length=40)
  title=models.CharField(verbose_name=u'Заголовок',max_length=100)
  post_text=models.TextField(verbose_name=u'Текст')
  tags=models.ManyToManyField(Tag,verbose_name=u'Тэг')
  pub_date=models.DateTimeField(verbose_name=u'Дата',auto_now_add='True')
  category=models.ForeignKey(Category)
  rating=models.IntegerField(verbose_name=u'Рейтинг',default=0)
  description=models.CharField(verbose_name=u'Description',max_length=200,blank='True')
  keywords=models.CharField(verbose_name=u'Keywords',max_length=80,blank='True')
  def save(self,*args,**kwargs):
    self.slug=slugify(self.title)
    super(Post, self).save(*args,**kwargs)
  
  def __unicode__(self):
    return self.title
    
  def get_url(self):
    return '/%s/' % (self.slug)
    
  def get_date(self):
    self.date=datetime.datetime.now()
     
  class Meta:
    ordering=['-pub_date']

class IptablePost(models.Model):
   client_ip=models.CharField(verbose_name=u'Ip клиента',max_length=20)
   item=models.ForeignKey(Post)

class IptableComment(models.Model):
   client_ip=models.CharField(verbose_name=u'Ip клиента',max_length=20)
   item=models.ForeignKey(Comment)

def get_url(self):
   post=Post.objects.get(id=self.object_pk)
   url=post.get_url()
   return url

def get_title(self):
   post=Post.objects.get(id=self.object_pk)
   title=post.title
   return title

#манки патчинг#
Comment.add_to_class('rating', models.IntegerField(verbose_name=u'Рейтинг',default=0))
Comment.add_to_class('comment',forms.CharField(label=u'Комментарий', widget=forms.Textarea(attrs={'rows':9, 'cols':60,'wrap':'soft'})))
Comment.add_to_class('get_url',get_url)
Comment.add_to_class('get_title',get_title)