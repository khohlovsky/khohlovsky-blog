from django.contrib import admin
from blogshot.models import *
from lightcomments.models import *
from tinymce.widgets import TinyMCE
from mce_filebrowser.admin import MCEFilebrowserAdmin

class TagAdmin(admin.ModelAdmin):
  list_display=('title',)
  #prepopulated_fields = {"slug": ("title",)}
  fields=('title','description')

class CategoryAdmin(admin.ModelAdmin):
  list_display=('title','image')
  #prepopulated_fields = {"slug": ("title",)}
  fields=('title','description','image')
  
class PostAdmin(MCEFilebrowserAdmin):
  list_display=('title','pub_date','rating')
  list_filter=('pub_date',)
  date_hierarchy='pub_date'
  fields=('title','post_text','tags','category','keywords','description',)
  filter_horizontal=('tags',)
  #prepopulated_fields = {"slug": ("title",)}
  formfield_overrides = {models.TextField: {'widget':TinyMCE(attrs={'cols': 80, 'rows': 30})}}

class CommentAdmin(admin.ModelAdmin):
  list_display=('post',)
  #prepopulated_fields = {"slug": ("title",)}
  fields=('nick','message','post','rating',)

  
admin.site.register(Tag,TagAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment,CommentAdmin)
