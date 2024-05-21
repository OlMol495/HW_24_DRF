from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views.course import CourseViewSet
from materials.views.lesson import (LessonCreateAPIView, LessonListAPIView, LessonUpdateAPIView,
                                    LessonDestroyAPIView, LessonRetrieveAPIView)
from materials.views.subscription import SubscriptionAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-detail'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
                  path('subscription/', SubscriptionAPIView.as_view(), name='subscription'),
              ] + router.urls
