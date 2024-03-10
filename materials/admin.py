from django.contrib import admin
from materials.models import Course, Lesson


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('title', 'description', 'image',)


@admin.register(Lesson)
class AdminLesson(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'video_link', 'course',)