from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'count_text']

    def count_text(self, post):
        return '{}글자'.format(len(post.text))
    count_text.short_description = '내용 글자 수'

admin.site.register(Post, PostAdmin)
 