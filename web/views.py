from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping

from web.models import *


@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def home(self, request):
        # 나의 영화 관심사 장르 모아 둔 dict
        theme_dict = {"romance":0,"fantasy":0,"thriller":0,
                      "comedy":0,"sf":0,"horror":0,
                      "mystery":0,"documentary":0,"animation":0}
        context = {}

        # 로그인 되었을 때, 나의 영화 관심사 장르를 나타낼 수 있다.
        try:
            review = Review.objects.select_related('userid', 'movieid');
            member = Member.objects.get(userid=request.session['sessionid'])

            max_value = self.findRatingCount(review,member,theme_dict)

            my_favorite_genre = self.createMyFavoriteGenreList(theme_dict, max_value)

            my_favorite_genre_name = self.findMyFavoriteGenreName(my_favorite_genre)
            context['favorite_genre'] = my_favorite_genre_name

            # 나의 영화 관심사 장르 포스터 리스트를 만들어 context를 통해 html으로 보내주기 위한 로직
            genre = Genre.objects.get(theme=my_favorite_genre_name)
            movie = Movie.objects.select_related('genreid')
            movie_poster_list = []
            for item in movie:
                if item.genreid == genre:
                    movie_poster_list.append(item.poster)
                    print(item.poster)
            print(movie_poster_list)
            context['poster_active'] = movie_poster_list[0]
            context['poster_list'] = movie_poster_list[1:]
        except: # 로그인이 되어있지 않을 때, 관심사를 나타내지 않는다.
            print("회원 x")
            pass
        return render(request, 'home.html', context);

    def findRatingCount(self, review, member, theme_dict):
        # 나의 영화 장르 별 별점을 부여한 영화 개수를 파악(그 중 가장 높은 영화 리턴)
        for item in review:
            if item.userid == member:
                movie = Movie.objects.select_related('genreid')
                for mov in movie:
                    if mov == item.movieid:
                        theme_dict[mov.genreid.theme] += 1
        return max(theme_dict.values())

    def createMyFavoriteGenreList(self, theme_dict, max_value):
        # 내가 가장 좋아하는 영화 관심사 장르를 모아두는 리스트
        # 내가 가장 좋아하는 : 장르마다 평점을 부여하는데, 평점을 부여한 영화 개수가 많은 것
        my_favorite_genre = []
        for (k, v) in theme_dict.items():
            if theme_dict[k] == max_value:
                my_favorite_genre.append(k)
        return my_favorite_genre

    def findMyFavoriteGenreName(self, my_favorite_genre):
        # 내가 가장 좋아하는 영화 관심사 장르가 복수이거나 하나일 때 조건
        # 하나일 때는 그 하나의 관심사 장르가 나의 영화 관심사 장르
        # ex)
        #   가장 많이 평점을 준 영화 장르가 복수일 때
        #   comedy : 2, animation : 2
        #   comedy 평균 평점 : 5.0
        #   animation 평균 평점 : 4.0
        #   comedy > animation => 나의 영화 관심사 장르
        # 반례)
        #   평균 평점이 같을 때 => animation : a, comedy : c => a>c : 나의 영화 관심사 장르는 comedy
        multi_favorite_genre = {}
        my_favorite_genre_name = ""
        if len(my_favorite_genre) > 1:
            for item in my_favorite_genre:
                avg_star = 0
                count_star = 0
                genre = Genre.objects.get(theme=item)
                review = Review.objects.select_related('userid', 'movieid')
                movie = Movie.objects.select_related('genreid')
                for rev in review:
                    for mov in movie:
                        if mov.genreid == genre:
                            if rev.movieid == mov:
                                avg_star += rev.star
                                count_star += 1

                multi_favorite_genre[genre.theme] = avg_star / count_star
            max_dict_value = max(multi_favorite_genre.values())
            for (k, v) in multi_favorite_genre.items():
                if v >= max_dict_value:
                    my_favorite_genre_name = k
                else:
                    continue
        else:
            my_favorite_genre_name = my_favorite_genre[0]
        return my_favorite_genre_name


    @request_mapping("/lv", method="get")
    def login(self, request):
        return render(request, 'user/login.html');

    @request_mapping("/loginimpl", method="post")
    def loginimpl(self, request):
        id = request.POST['id'];
        pwd = request.POST['pwd'];
        try:
            mem = Member.objects.get(userid=id)
            if mem.pwd == pwd:
                request.session['sessionid'] = mem.userid;
                return render(request, 'home.html');
            else:
                raise Exception;
        except:
            return render(request, 'user/loginfail.html');

    @request_mapping("/rv", method="get")
    def registerview(self, request):
        return render(request, 'user/register.html');

    @request_mapping("/registerimpl", method="post")
    def registerimpl(self, request):

        id = request.POST['id'];
        pwd = request.POST['pwd'];
        pwdcheck = request.POST['pwdc'];
        name = request.POST['name'];
        email = request.POST['mail'];
        phone = request.POST['phone'];
        birth = request.POST['birth'];
        gender = request.POST['gender'];
        idcheck = request.POST['Q'];
        idanswer = request.POST['A'];

        try:
            Member.objects.get(userid=id)
            return render(request, 'user/registerfail.html');
        except:
            if birth == '':
                return render(request, 'user/registerfail.html');
            elif pwd == pwdcheck:
                Member(userid=id, pwd=pwd, name=name, email=email,phone=phone, birthday=birth, gender=gender, checkq=idcheck,
                       checka=idanswer).save();
                return render(request, 'user/registerok.html');
            else:
                return render(request, 'user/registerfail.html');

    @request_mapping("/lo", method="get")
    def logout(self, request):
        if request.session['sessionid'] != None:
            del request.session['sessionid'];

        return render(request, 'home.html');

    @request_mapping("/uf/<str:id>", method="get")
    def userinfo(self, request, id):
        obj = Member.objects.get(userid=id);
        context = {'obj': obj};
        return render(request, 'user/userinfo.html', context);

    @request_mapping("/deluser", method="get")
    def deluser(self, request):
        id = request.session['sessionid']
        id2 = Member.objects.get(userid=id)
        if request.session['sessionid'] != None:
            del request.session['sessionid'];
        id2.delete();
        return render(request, 'user/deleted.html');

    @request_mapping("/chuser", method="get")
    def chuser(self, request):
        id = request.session['sessionid'];
        obj = Member.objects.get(userid=id);
        context = {'obj': obj};
        return render(request, 'user/changeinfo.html', context);

    @request_mapping("/changeimpl", method="post")
    def changeimpl(self, request):
        id = request.POST['id'];
        pwd = request.POST['pwd'];
        pwdc = request.POST['pwdc'];
        name = request.POST['name'];
        email = request.POST['mail'];
        phone = request.POST['phone'];
        birth = request.POST['birth'];
        gender = request.POST['gender'];
        Q = request.POST['Q'];
        A = request.POST['A'];

        Member.objects.get(userid=id)
        if pwd == pwdc:
            Member(userid=id, pwd=pwd, name=name, email=email, phone=phone, birthday=birth, gender=gender, checkq=Q,
                   checka=A).save();
            return render(request, 'user/changeok.html');
        else:
            return render(request, 'user/changefail.html');

    @request_mapping("/find", method="get")
    def find(self, request):
        return render(request, 'user/find1.html');

    @request_mapping("/findimpl1", method="post")
    def findimpl1(self, request):
        id = request.POST['id'];
        try:
            obj = Member.objects.get(userid=id);
            context = {'obj': obj};
            return render(request, 'user/find2.html', context);
        except:
            return render(request, 'user/findfail1.html');

    @request_mapping("/findimpl2", method="post")
    def findimpl2(self, request):
        A = request.POST['A'];
        try:
            obj = Member.objects.get(checka=A)
            context = {'obj': obj};
            return render(request, 'user/findok.html', context);
        except:
            return render(request, 'user/findfail2.html');