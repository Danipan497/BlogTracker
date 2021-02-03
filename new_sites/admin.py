from django.contrib import admin

from new_sites.models import Topic, Entry, Article, ArticleEntry, Comment


class TopicAdmin(admin.ModelAdmin):
    list_display = ('text',)


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(ArticleEntry)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry)

