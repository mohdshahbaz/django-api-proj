from django.urls import path
from .views import AddAdvisorView, BookACallView, GetBookedCalls, LoginView, RegisterView, RetrieveAdvisorView

urlpatterns = [
    path('user/register/', RegisterView.as_view()),
    path('user/login/', LoginView.as_view()),
    path('admin/advisor/', AddAdvisorView.as_view()),
    path('user/<int:user>/advisor/', RetrieveAdvisorView.as_view()),
    path('user/<int:user>/advisor/<int:advisor>/', BookACallView.as_view()),
    path('user/<int:user>/advisor/booking/', GetBookedCalls.as_view())
]
