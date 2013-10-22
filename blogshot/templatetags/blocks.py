from blogshot.models import Tag, Category, Post
from blogshot.forms import LoginForm
from django import template
from lightcomments.models import Comment

register = template.Library()

def all_tags():
   tags=Tag.objects.all()
   return {'tags':tags}

def all_cat():
   cats=Category.objects.all()
   return {'cats':cats,}

def auth_form():
   login_form=LoginForm()
   return {'login_form':login_form,}

def most_rated():
   posts=Post.objects.all()
   posts_rated=posts.order_by('rating')
   return {'posts_rated':posts_rated[:10],}

def last_comments():
   comm=Comment.objects.all()
   last=comm.order_by('-pub_date')
   return {'comments':last[:10],}


register.inclusion_tag('tags_block.html')(all_tags)
register.inclusion_tag('cat_block.html')(all_cat)
register.inclusion_tag('most_rated_block.html')(most_rated)
#register.inclusion_tag('login_form.html')(auth_form)
register.inclusion_tag('last_comm_block.html')(last_comments)

