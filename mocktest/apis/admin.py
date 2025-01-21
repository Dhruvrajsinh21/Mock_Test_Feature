from django.contrib import admin
from .models import Question, MockTest, Answer

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_option')
    search_fields = ('text',)

admin.site.register(Question, QuestionAdmin)

class MockTestAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_time',)
    list_filter = ('user',)
    search_fields = ('user__username',)

admin.site.register(MockTest, MockTestAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'mock_test', 'question', 'user_answer')
    list_filter = ('mock_test',)
    search_fields = ('user__username', 'question__text')

admin.site.register(Answer, AnswerAdmin)
