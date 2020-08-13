from django.db import models
class BlogPost(models.Model):
    # 博客标题
    title=models.CharField(max_length=150)
    # 博客正文
    body=models.TextField()
    # 博客创建时间
    timestamp=models.DateTimeField()
# Create your models here.
