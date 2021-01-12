from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.

class Article(models.Model):
    owner = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)
    highlight =  models.TextField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)