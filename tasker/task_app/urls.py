from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet, PersonViewSet, PersonTasksView, PersonTasksStatusView


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'persons', PersonViewSet)

urlpatterns = [
    path('persons/<int:pk>/tasks/', PersonTasksView.as_view(), name='person-tasks'),
    path('persons/<int:pk>/tasks/<str:status>/', PersonTasksStatusView.as_view(), name='person-tasks-status'),
    path('', include(router.urls)),
]