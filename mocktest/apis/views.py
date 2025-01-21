# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MockTest, UserMockTest, Question
from .serializers import QuestionSerializer
from django.contrib.auth.models import User

class AddQuestionView(APIView):
    def post(self, request):
        """
        Endpoint to add new questions to the system.
        """
        question_data = request.data
        serializer = QuestionSerializer(data=question_data)
        
        if serializer.is_valid():
            serializer.save()  # Saves the new question
            return Response({'message': 'Question added successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StartMockTestView(APIView):
    def get(self, request, mock_test_id):
        user = request.user  # Get the current authenticated user
        try:
            mock_test = MockTest.objects.get(id=mock_test_id)
        except MockTest.DoesNotExist:
            return Response({"message": "Mock test not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Get all questions that the user hasn't answered yet
        answered_questions = UserMockTest.objects.filter(user=user, mock_test=mock_test).values_list('answered_questions', flat=True)
        questions = mock_test.questions.exclude(id__in=answered_questions)

        question_serializer = QuestionSerializer(questions, many=True)
        return Response(question_serializer.data, status=status.HTTP_200_OK)

class SubmitMockTestAnswersView(APIView):
    def post(self, request, mock_test_id):
        user = request.user
        try:
            mock_test = MockTest.objects.get(id=mock_test_id)
        except MockTest.DoesNotExist:
            return Response({"message": "Mock test not found."}, status=status.HTTP_404_NOT_FOUND)
        
        answers = request.data.get('answers')  # Expected format: [{'question_id': 1, 'answer': 'A'}, ...]
        user_mock_test, created = UserMockTest.objects.get_or_create(user=user, mock_test=mock_test)

        score = 0
        answered_questions = []

        for answer in answers:
            try:
                question = Question.objects.get(id=answer['question_id'])
            except Question.DoesNotExist:
                return Response({"message": f"Question with id {answer['question_id']} not found."}, status=status.HTTP_404_NOT_FOUND)
            
            if question.correct_answer == answer['answer']:
                score += 1
            answered_questions.append(question)

        user_mock_test.answered_questions.add(*answered_questions)
        user_mock_test.save()

        return Response({
            'score': score,
            'total_questions': len(answers),
            'answered_questions': len(answered_questions)
        }, status=status.HTTP_200_OK)

class GetTestResultsView(APIView):
    def get(self, request, mock_test_id):
        user = request.user
        try:
            mock_test = MockTest.objects.get(id=mock_test_id)
        except MockTest.DoesNotExist:
            return Response({"message": "Mock test not found."}, status=status.HTTP_404_NOT_FOUND)
        
        user_mock_test = UserMockTest.objects.filter(user=user, mock_test=mock_test).first()
        if not user_mock_test:
            return Response({"message": "Test not started yet!"}, status=status.HTTP_400_BAD_REQUEST)

        questions = user_mock_test.answered_questions.all()
        question_serializer = QuestionSerializer(questions, many=True)

        return Response({
            'questions': question_serializer.data,
            'score': len(questions),  # Assuming 1 point per correct answer
            'total_questions': mock_test.questions.count()
        }, status=status.HTTP_200_OK)
