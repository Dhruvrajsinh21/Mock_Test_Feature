from django.urls import path
from .views import StartMockTestView, SubmitMockTestAnswersView, GetTestResultsView

urlpatterns = [
    path('mock_test/<int:mock_test_id>/start/', StartMockTestView.as_view(), name='start_mock_test'),
    path('mock_test/<int:mock_test_id>/submit/', SubmitMockTestAnswersView.as_view(), name='submit_mock_test_answers'),
    path('mock_test/<int:mock_test_id>/results/', GetTestResultsView.as_view(), name='get_test_results'),
]
