from django.db import models


class Todo(models.Model):

    class Meta:
        verbose_name = ('Todo')
        verbose_name_plural = ('Todos')

    title = models.CharField(max_length=255, default='')
    contents = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(verbose_name='作成時間', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Todo_detail', kwargs={'pk': self.pk})
