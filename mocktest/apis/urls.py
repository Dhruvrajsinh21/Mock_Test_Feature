from django.urls import path
from .views import StartMockTest, SubmitAnswer, RegisterUser, LoginUser

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('start_mock_test/', StartMockTest.as_view(), name='start_mock_test'),
    path('submit_answer/<int:question_id>/', SubmitAnswer.as_view(), name='submit_answer'),
]
