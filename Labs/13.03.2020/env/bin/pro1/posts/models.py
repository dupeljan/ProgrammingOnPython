from django.db import models

# Create your models here.

class Meta:
	db_table = 'posts'

class Post(models.Model):
	title = models.CharField(max_length = 120, verbose_name = 'заголовок')
	content = models.TextField(verbose_name = 'Текст сообщения')
	timestamp = models.DateTimeField(verbose_name = 'Время создания')
	updated = models.DateTimeField(verbose_name = 'Время обновления')
	id = models.AutoField(primary_key = True)
	post_likes = models.IntegerField(default = 0, verbose_name = 'Лайков')
	genre = (('r1','Роман'),('p','Поэма'),('r2','Рассказ'))
	genre = models.CharField(max_length = 120, verbose_name = 'Жанр',choices = genre, default = 'r1')
	post_author = models.ForeignKey('Author',null = True, blank = True)
	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

class Author(models.Model):
	id = models.AutoField(primary_key = True)
	first_name = models.TextField(verbose_name = 'Первое имя')
	second_name = models.TextField(verbose_name = 'Второе имя')
	email = models.EmailField(verbose_name = 'Почта')

	def __unicode__(self):
		return self.first_name + " " + self.second_name

	def __str__(self):
		return self.first_name + " " + self.second_name

class Comment(models.Model):
	id = models.AutoField(primary_key = True)
	comment_text = models.TextField(verbose_name = 'Комментарий')
	comment_article = models.ForeignKey(Post, verbose_name = 'К посту')

	def __unicode__(self):
		return self.comment_text

	def __str__(self):
		return self.comment_text
