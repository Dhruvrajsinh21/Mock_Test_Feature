from django.contrib import admin
from .models import Question, MockTest, UserMockTest

admin.site.register(Question)
admin.site.register(MockTest)
admin.site.register(UserMockTest)
