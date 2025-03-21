from django.db import models

class Films(models.Model):
	name = models.CharField('Название фильма', max_length=100)
	description = models.TextField('Описание фильма')
	review = models.TextField('Отзыв о фильме')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Фильм'
		verbose_name_plural = 'Фильмы'