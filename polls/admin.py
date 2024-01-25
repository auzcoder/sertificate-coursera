from django.contrib import admin
from polls.models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice_text']
