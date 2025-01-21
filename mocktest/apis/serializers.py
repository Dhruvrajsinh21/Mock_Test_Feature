from rest_framework import serializers
from .models import MockTest, Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'option_1', 'option_2', 'option_3', 'option_4']


class MockTestSerializer(serializers.ModelSerializer):
    questions_answered = QuestionSerializer(many=True)

    class Meta:
        model = MockTest
        fields = ['id', 'user', 'questions_answered', 'start_time']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['user', 'mock_test', 'question', 'user_answer']
