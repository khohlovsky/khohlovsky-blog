#coding:utf-8

from datetime import datetime
from models import Post, Category, Tag, IptablePost,IptableComment
from lightcomments.models import Comment
from lightcomments.form import CommentForm
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib import auth
from django.template import RequestContext
from forms import LoginForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from headshot import settings
from django.http import HttpResponse


def post (request,slug):
   try:
      query=Post.objects.get(slug=slug)
      tags=query.tags.all()
      comments=Comment.objects.filter(post=query.id)
   except Post.DoesNotExist:
      raise Http404()
   return render_to_response('post.html',{'post':query,'tags':tags,'comments':comments,'CommentForm':CommentForm,},context_instance=RequestContext(request))

def lists(request,slug,url):
   if url == 'category':
      try:
	 posts=Category.objects.get(slug=slug)
      except Post.DoesNotExist:
	 raise Http404()
      result=posts.post_set.order_by('-pub_date')
      title=posts.title
   elif url == 'tag':
      try:
	 posts=Tag.objects.get(slug=slug)
      except Post.DoesNotExist:
	 raise Http404()
      result=posts.post_set.order_by('-pub_date')
      title=posts.title
   else:
      result=Post.objects.order_by('-pub_date')
      title='Lazy man blog'
   paginator=Paginator(result,settings.PAGINATOR)
   page = request.GET.get('page')
   try:
      page_posts=paginator.page(page)
   except PageNotAnInteger:
      page_posts = paginator.page(1)
   except EmptyPage:
      page_posts=paginator.page(1)
   return render_to_response('index.html',{'posts':page_posts,'title':title,},context_instance=RequestContext(request))

def save(request,model):
   if request.method == 'POST':
      ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
      this_id=request.POST.get('slug',) or request.POST.get('id',)
      funct=request.POST.get('funct',)
      if model.__name__=='IptableComment':
	 thismod=Comment.objects.get(id=this_id)
      if model.__name__=='IptablePost':
	 thismod=Post.objects.get(slug=this_id)
      i=model.objects.filter(client_ip=ip,item=thismod)
      if i:
	 rating='null'
      else:
	 this_table=model(client_ip=ip,item=thismod)
	 this_table.save()
	 if funct=='plus':
	    thismod.rating+=1
	    thismod.save()
	 if funct=='minus':
	    thismod.rating-=1
	    thismod.save()
	 rating=str(thismod.rating)
      return HttpResponse(rating)


def comment_save(request):
    if request.is_ajax():
        nick=request.POST.get('nick')
        message=request.POST.get('message')
        slug=request.POST.get('slug')
        try:
            post=Post.objects.get(slug=slug)
            comment=Comment(nick=nick,message=message,post_id=post.id)
            comment.save()
        except error:
            HttpREsponse("false")
        return HttpResponse(200)
