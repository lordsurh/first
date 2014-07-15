from django.contrib import admin
from Order.models import *
class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Poll Question ',       {'fields':['question'], 'classes': ['collapse']}),
        ('Date information',     {'fields':['pub_date'] , 'classes': ['collapse']}),
        ('Poll section ',       {'fields':['poll__section'], 'classes': ['collapse']}),

    ]
    inlines = [ChoiceInLine]
    list_display = ('question' , 'pub_date' , 'poll__section' , 'was__published__recently')
    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Poll ,PollAdmin )
admin.site.register(Voter )

