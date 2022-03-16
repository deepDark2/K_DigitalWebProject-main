import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping
from django.db.models import Sum
from web.models import *


@request_mapping("/board")
class BoardView(View):

    @request_mapping("/", method="get")
    def home(self,request):
        try:
            boards = Board.objects.all()
            # 입력 파라미터
            page = request.GET.get('page', '1')  # 페이지

            # 조회
            question_list = Board.objects.order_by('-write_date')

            # 페이징처리
            paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
            page_obj = paginator.get_page(page)

            context = {
                'boards': boards,
                'question_list': page_obj
            }
        except:
            pass
        return render(request,'board.html',context);

    @request_mapping("/post", method="get")
    def writeBoard(self, request):
        return render(request, 'board_post.html');

    @request_mapping("/postimpl", method="post")
    def postData(self, request):
        try:
            title = request.POST['title']
            content = request.POST['content']
            if title == "" or content == "":
                raise Exception
            member = Member.objects.get(userid=request.session['sessionid'])
            print(title,content)
            board = Board(userid=member,title=title,content=content)
            board.save()
            html = '/board'
        except:
            html = '/board/post'
        return redirect(html);

    @request_mapping("/<int:pk>/", method="get")
    def detailBoard(self, request, pk):
        context = {}
        try:
            board = Board.objects.get(boardid=pk)
            board.read_count += 1
            board.save()
            context['board'] = board
        except:
            print("오류!")
        return render(request, 'board_detail.html', context);

    @request_mapping("/<int:pk>/edit/<int:pk2>", method="get")
    def editBoardView(self, request, pk,pk2):
        board = Board.objects.get(boardid=pk)
        return render(request, 'board_edit.html', {'board': board})

    @request_mapping("/<int:pk>/delete", method="get")
    def delteBoard(self, request, pk):
        board = Board.objects.get(boardid=pk)
        board.delete();
        return redirect('/board/');

    @request_mapping("/<int:pk>/edit/<int:pk2>/impl", method="post")
    def editBoard(self, request, pk,pk2):
        board = Board.objects.get(boardid=pk)
        try:
            if request.method == "POST":
                title = request.POST['title']
                content = request.POST['content']
                if title == "" and content == "":
                    raise Exception
                board.title = title
                board.content = content
                board.save()
                return redirect('/board/')
        except:
            return redirect('/board/' + str(pk) + '/edit/' + str(pk))

    @request_mapping("/<int:pk>/vote/<int:pk2>", method="get")
    def vote(self, request, pk, pk2):
        userid = request.session['sessionid'];
        try:
            Voter.objects.filter(reviewid=pk);
            if Voter.objects.filter(memberid = userid):
                return render(request, 'recommendfail.html');
            else:
                pass;
        except:
            Voter(reviewid=pk, memberid=userid, recommend=1).save();
            return redirect('/board/' + str(pk))


