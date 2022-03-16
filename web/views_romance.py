from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping

from web.models import *


@request_mapping("/romance")
class RomanceView(View):

    @request_mapping("/", method="get")
    def home(self,request):
        objs = Movie.objects.select_related('genreid');
        genre = Genre.objects.get(genreid=1)
        context = {
            'objs': objs,
            'genre': genre
        };
        return render(request,'movie-overview.html', context);
