from django.contrib import admin
from .models import Measurement,Workouts,UserProgress,WorkoutPlans,UserProfile

class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('user', 'height', 'weight', 'age', 'bmi', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('created_at',)
    
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'unique_title_days', 'no_days')
    search_fields = ('user__username', 'unique_title_days__title')
    list_filter = ('unique_title_days__days',)

class WorkoutPlansAdmin(admin.ModelAdmin):
    list_display = ('title', 'days', 'description')
    search_fields = ('title',)
    list_filter = ('days',)

admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(Workouts)
admin.site.register(UserProfile)
admin.site.register(UserProgress,UserProgressAdmin)
admin.site.register(WorkoutPlans,WorkoutPlansAdmin)
