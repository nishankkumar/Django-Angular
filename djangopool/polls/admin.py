from django.contrib import admin

# Register your models here.
from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

admin.site.register(Choice)
# admin.site.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

# admin.site.register(Question, QuestionAdmin)

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]

admin.site.register(Question, QuestionAdmin)

