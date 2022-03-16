from django.contrib import admin
from web.models import *
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('userid','pwd','name','email','birthday','gender','checkq','checka')

class GenreAdmin(admin.ModelAdmin):
    list_display = ('genreid','theme')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewid','userid','movieid','star')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('movieid','genreid','poster','title',
                    'open_date','grade','running_time','director','actor',
                    'open_country','trailer','summary')

class BoardAdmin(admin.ModelAdmin):
    # list_display = ('boardid','userid','movieid','title','content',
    #                 'write_date','read_count')
    list_display = ('boardid', 'userid', 'title', 'content',
                    'write_date', 'read_count')

admin.site.register(Member, MemberAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Board, BoardAdmin)
