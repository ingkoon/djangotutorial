from django.db import models

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.
owner = models.ForeignKey('auth.USer', related_name='orly')
highlighted = models.TextField()

