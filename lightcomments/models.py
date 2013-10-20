#encoding:utf-8
from django.db import models

# Create your models here.
class Comment(models.Model):
    post=models.ForeignKey('blogshot.Post')
    pub_date=models.DateTimeField(verbose_name=u'Время',auto_now_add='True')
    nick=models.CharField(verbose_name=u'Ник',max_length=30)
    rating= models.IntegerField(verbose_name=u'Рейтинг',default=0)
    message=models.TextField(verbose_name=u'Сообщение',)

    def get_url(self):
        post=Post.objects.get(id=self.object_pk)
        url=post.get_url()
        return url

    def get_title(self):
        post=Post.objects.get(id=self.object_pk)
        title=post.title
        return title
    def __unicode__(self):
        return self.nick
