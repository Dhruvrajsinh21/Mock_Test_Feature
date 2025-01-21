from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Question(models.Model):
    text = models.CharField(max_length=255, default="Sample Question")
    option_1 = models.CharField(max_length=100, default="Option 1")
    option_2 = models.CharField(max_length=100, default="Option 2")
    option_3 = models.CharField(max_length=100, default="Option 3")
    option_4 = models.CharField(max_length=100, default="Option 4")
    correct_option = models.CharField(max_length=100, default="Option 1")  # Assuming Option 1 is correct by default

    def __str__(self):
        return self.text


class MockTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    questions_answered = models.ManyToManyField(Question, blank=True)
    start_time = models.DateTimeField(default=timezone.now)  # Default to the current time

    def __str__(self):
        return f"Mock Test for {self.user.username if self.user else 'Unknown User'}"


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    mock_test = models.ForeignKey(MockTest, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=100, default="Option 1")  # Default answer to Option 1

    def __str__(self):
        return f"Answer by {self.user.username} for {self.question.text}"
