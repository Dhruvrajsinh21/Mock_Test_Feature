from rest_framework import serializers
from .models import Question, MockTest, UserMockTest
from django.contrib.auth.models import User

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'answer']

class MockTestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = MockTest
        fields = ['id', 'name', 'questions']

class UserMockTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMockTest
        fields = ['user', 'mock_test', 'answered_questions']
