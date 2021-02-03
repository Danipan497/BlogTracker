from django.contrib import admin

from new_sites.models import Topic, Entry


class TopicAdmin(admin.ModelAdmin):
    list_display = ('text',)


admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry)



