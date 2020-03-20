from django.contrib import admin
from .models import Post
from .models import Author
from .models import Comment

# Register your models here.

class PostInstanceInline(admin.StackedInline):
	model = Comment
	extra = 1

class PostModelAdmin(admin.ModelAdmin):
	list_display = ['title','timestamp','updated']
	list_display_links = ['title','timestamp','updated']
	list_filter = ['timestamp']
	inlines = [PostInstanceInline]
	ordering = ['-timestamp']
	# fields = ('title','content')
	# exclude = ('likes',)
#	list_editable = [#smth pole not exists in list_display_links]
	class Meta:
		model = Post

class AuthorModelAdmin(admin.ModelAdmin):
	list_display = ['first_name','second_name','email']
	list_filter = ['first_name']
	ordering = ['second_name','first_name']
	class Meta:
		model = Author

class CommentModelAdmin(admin.ModelAdmin):
	list_display = ['comment_text','comment_article']
	class Meta:
		model = Comment

admin.site.register(Post,PostModelAdmin)
admin.site.register(Author,AuthorModelAdmin)
admin.site.register(Comment,CommentModelAdmin)