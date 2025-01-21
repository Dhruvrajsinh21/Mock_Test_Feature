# urls.py
from django.urls import path
from .views import AddQuestionView, StartMockTestView, SubmitMockTestAnswersView, GetTestResultsView

urlpatterns = [
    path('questions/add/', AddQuestionView.as_view(), name='add-question'),
    path('mock_test/<int:mock_test_id>/start/', StartMockTestView.as_view(), name='start-mock-test'),
    path('mock_test/<int:mock_test_id>/submit/', SubmitMockTestAnswersView.as_view(), name='submit-mock-test-answers'),
    path('mock_test/<int:mock_test_id>/results/', GetTestResultsView.as_view(), name='get-test-results'),
]
