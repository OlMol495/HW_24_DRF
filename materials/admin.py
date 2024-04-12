from django.contrib import admin
from materials.models import Course, Lesson, Subscription
from payments.admin import AdminCoursePrice


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('title', 'description', 'image',)
    inlines = (AdminCoursePrice,)


@admin.register(Lesson)
class AdminLesson(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'video_link', 'course',)

@admin.register(Subscription)
class AdminSubscription(admin.ModelAdmin):
    list_display = ('user', 'course',)
