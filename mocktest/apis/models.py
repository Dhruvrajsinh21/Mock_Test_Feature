# models.py
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=512)
    option_a = models.CharField(max_length=128)
    option_b = models.CharField(max_length=128)
    option_c = models.CharField(max_length=128)
    option_d = models.CharField(max_length=128)
    answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

    def __str__(self):
        return self.question_text

class MockTest(models.Model):
    title = models.CharField(max_length=256)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title


class UserMockTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mock_test = models.ForeignKey(MockTest, on_delete=models.CASCADE)
    answered_questions = models.ManyToManyField(Question)

    def __str__(self):
        return f"UserMockTest for {self.user.username} on {self.mock_test.title}"
