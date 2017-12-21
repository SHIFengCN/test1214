from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice.questions.through
    #extra = 3

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['choice_text']}),
    ]
    list_display = ('choice_text',)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    #增加筛选器
    search_fields = ['question_text']
    #增加搜索框
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)