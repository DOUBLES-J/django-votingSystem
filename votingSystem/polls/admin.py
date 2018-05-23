from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class ChoiceAdmin(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceAdmin]
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.site_header = 'Django DL'
admin.site.site_title = 'DH'
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
