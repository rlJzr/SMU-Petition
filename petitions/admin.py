from django.contrib import admin
from petitions.models import Petition, Comment, Answer


class PetitionAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']
    list_display = ['status', 'anonymous', 'author', 'subject', 'content', 'category', 'create_date', 'modify_date', 'end_date']


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['petition__subject']
    list_display = ['author', 'petition', 'content', 'create_date', 'modify_date']


class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['petition__subject']
    list_display = ['author', 'petition', 'content', 'create_date', 'modify_date']


admin.site.register(Petition, PetitionAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Answer, AnswerAdmin)
