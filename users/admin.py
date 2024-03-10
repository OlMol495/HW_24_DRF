from django.contrib import admin
from users.models import User, Payment


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('email', 'phone', 'city', 'avatar',)


@admin.register(Payment)
class AdminPayment(admin.ModelAdmin):
    list_display = ('user', 'payment_date', 'course', 'lesson', 'amount', 'payment_method',)