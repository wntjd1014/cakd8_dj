import os
from django.db import models
from django.contrib.auth.models import User
# from markdownx.models import MarkdownxField
# from markdownx.utils import markdown

# class Tag(models.Model):
#     name = models.CharField(max_length=50)
#     slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return f'/blog/tag/{self.slug}/'
        
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'categories'

# Post는 기본 구조이다.
class Post(models.Model):
    # 장고 방식으로 형태 바꿔줌
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    # 생성해주자.
    # 현재의 시간을 자동으로 추가해주기.
    created_at = models.DateTimeField(auto_now_add=True)
    # 자동으로 업데이트
    updated_at = models.DateTimeField(auto_now=True)


    # # 작성자
    # # ForeignKey는 연결 시켜서 없애줄때 같이 없애기 위함.
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # # 카테고리
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    # tags = models.ManyToManyField(Tag, blank=True)

    # 초기화
    # pk는 포스트의 제목이 나오도록 함.
    # 자동으로 생성되는 번호인데 각 레코드에 대한 고유값으로 자동으로 생성되는 번호이다.
    # 처음에는 1이 자동으로 부여되고 1씩 증가한다.
    def __str__(self):
        return f'[{self.pk}]{self.title}'

    # 객체의 상세 페이지로 이동할 수 있는 링크를 만들 수 있다.
    # url 생성 규칙을 정의하는 매서드
    # 블로그/1 이런식으로 url을 만들어준다.
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    
#     # 파일 확장자 얻는거
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

    # def get_content_markdown(self):
    #     return markdown(self.content)

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f'{self.author}::{self.content}'

#     def get_absolute_url(self):
#         return f'{self.post.get_absolute_url()}#comment-{self.pk}'
    