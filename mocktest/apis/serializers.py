# serializers.py
from rest_framework import serializers
from .models import Question, MockTest, UserMockTest

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'options', 'correct_answer']

class MockTestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = MockTest
        fields = ['id', 'title', 'questions']
