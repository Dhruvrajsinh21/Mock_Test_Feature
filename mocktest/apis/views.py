from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models import MockTest, Question, Answer
from .serializers import MockTestSerializer, AnswerSerializer, QuestionSerializer
from random import sample

class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"message": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"message": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)

        return Response({
            "message": f"User {user.username} created successfully"
        }, status=status.HTTP_201_CREATED)


class LoginUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"message": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(password):
            return Response({"message": "Incorrect password"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "message": f"User {user.username} logged in successfully"
        }, status=status.HTTP_200_OK)


class StartMockTest(APIView):
    def get(self, request):
        user_id = request.query_params.get('user', None)

        if not user_id:
            user = User.objects.first()
            if not user:
                return Response({"detail": "No users found."}, status=400)
            print(f"Using default user: {user.id}")
        else:
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        mock_test, created = MockTest.objects.get_or_create(user=user)

        if created:
            answered_questions = Answer.objects.filter(mock_test=mock_test).values_list('question', flat=True)
            available_questions = Question.objects.exclude(id__in=answered_questions)

            questions_to_ask = sample(list(available_questions), min(10, available_questions.count()))

            for question in questions_to_ask:
                mock_test.questions_answered.add(question)

            mock_test.refresh_from_db()

        serializer = MockTestSerializer(mock_test)
        return Response(serializer.data, status=200)


class SubmitAnswer(APIView):
    def post(self, request, question_id):
        user_id = request.query_params.get('user', None)

        if not user_id:
            return Response({"detail": "User parameter is missing."}, status=400)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        user_answer = request.data.get('user_answer')

        if not user_answer:
            return Response({"message": "Answer is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            return Response({"message": "Question not found"}, status=status.HTTP_404_NOT_FOUND)

        mock_test, created = MockTest.objects.get_or_create(user=user)

        answer = Answer.objects.create(
            user=user,
            mock_test=mock_test,
            question=question,
            user_answer=user_answer
        )

        return Response({"message": "Answer submitted successfully"}, status=status.HTTP_201_CREATED)
