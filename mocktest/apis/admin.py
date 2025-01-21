from django.contrib import admin
from .models import Question, MockTest, Answer

# Register the Question model in the admin interface
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_option')  # Fields to display
    search_fields = ('text',)  # Enable searching by question text

admin.site.register(Question, QuestionAdmin)

# Register the MockTest model
class MockTestAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_time',)  # Display user and start time in the list
    list_filter = ('user',)  # Filter by user
    search_fields = ('user__username',)  # Search by the username of the user

admin.site.register(MockTest, MockTestAdmin)

# Register the Answer model
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'mock_test', 'question', 'user_answer')  # Display relevant fields
    list_filter = ('mock_test',)  # Filter by mock test
    search_fields = ('user__username', 'question__text')  # Search by username and question text

admin.site.register(Answer, AnswerAdmin)
