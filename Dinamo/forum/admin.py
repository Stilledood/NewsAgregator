from django.contrib import admin
from .models import Answers,Questions,Topics,Comment
from django.db.models import Count


@admin.register(Topics)
class TopicAdmin(admin.ModelAdmin):
    '''Class to construct a custom topic admin '''

    list_display = ['title','date_added','posted_by','comm_count']
    list_filter = ('date_added','posted_by')
    date_hierarchy = ('date_added')


    fieldsets = (
        ('Main',{'fields':('title',)}),
        ('Related',{'fields':('posted_by',)})
    )


    def get_queryset(self, request):
        queryset=super().get_queryset(request)
        return  queryset.annotate(comm_number=Count('comment'))

    def comm_count(self,topics):
        return topics.comm_number

    comm_count.short_description='Number of comments'
    comm_count.admin_order_field='comm_number'



@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    '''Class to construct a custom admin question view'''

    list_display = ['title','date_added','answer_count']
    list_filter = ('title','date_added')
    date_hierarchy = ('date_added')
    search_fields = ('title','author')

    fieldsets = (
        ('Main',{'fields':('title',)}),
        ('Related',{'fields':('author',)}),
    )

    def get_queryset(self,request):
        queryset=super().get_queryset(request)
        return queryset.annotate(answer_count=Count('answers'))

    def answer_count(self,questions):
        return questions.answer_count

    answer_count.short_description='Number of Answers'
    answer_count.admin_order_field='answer_count'














