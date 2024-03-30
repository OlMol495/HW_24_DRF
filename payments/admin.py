from django.contrib import admin


from payments.models import Payment, CoursePrice, LessonPrice


@admin.register(Payment)
class AdminPayment(admin.ModelAdmin):
    list_display = ('user', 'payment_date', 'course', 'lesson', 'amount', 'payment_method',)


class AdminCoursePrice(admin.StackedInline):
    model = CoursePrice
    list_display = ('pk', 'course', 'price',)

class AdminLessonPrice(admin.StackedInline):
    model = LessonPrice


admin.site.register(CoursePrice)
admin.site.register(LessonPrice)
