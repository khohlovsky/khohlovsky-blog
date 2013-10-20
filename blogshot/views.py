#coding:utf-8

from datetime import datetime
from models import Post, Category, Tag, IptablePost,IptableComment
from django.contrib import comments
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib import auth
from django.template import RequestContext
from forms import LoginForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from headshot import settings


def post (request,slug):
   try:
      query=Post.objects.get(slug=slug)
      tags=query.tags.all()
   except Post.DoesNotExist:
      raise Http404()
   return render_to_response('post.html',{'post':query,'tags':tags},context_instance=RequestContext(request))

def auth_view(request):
   form=LoginForm(request.POST or None)
   referer = request.META.get('HTTP_REFERER', '') or "/"
   if request.method=="POST" and form.is_valid():
      data=form.cleaned_data
      user=data['login']
      passwd=data['password']
      user=auth.authenticate(username=user, password=passwd)
      if user is not None and user.is_active:
	 auth.login(request,user)
	 return HttpResponseRedirect(referer)
      else:
	 return HttpResponseRedirect(referer)
   else:
      return HttpResponseRedirect(referer)

def logout_view(request):
   auth.logout(request)
   referer = request.META.get('HTTP_REFERER', '') or "/"
   return HttpResponseRedirect(referer)
   
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
	 thismod=comments.Comment.objects.get(id=this_id)
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
