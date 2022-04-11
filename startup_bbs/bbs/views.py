from django.shortcuts import render

#TODO:ここでDRF仕様のビュークラスと通常のビュークラスを切り替え
from django.views import View
#from rest_framework.views import APIView as View

from django.http.response import JsonResponse
from django.template.loader import render_to_string

from .models import Topic
from .forms import TopicForm


#未認証ユーザーはログイン画面へリダイレクト
#https://noauto-nolife.com/post/django-login-required-mixin/

from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):

        context             = {}
        context["topics"]   = Topic.objects.all()

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        json    = { "error":True }
        form    = TopicForm(request.POST)

        if not form.is_valid():
            print("Validation Error")
            print(form.errors)
            return JsonResponse(json)

        form.save()

        context             = {}
        context["topics"]   = Topic.objects.all()

        json["error"]   = False
        json["content"] = render_to_string("bbs/content.html",context,request)


        return JsonResponse(json)

    def delete(self, request, *args, **kwargs):
        
        json    = { "error":True }

        if "pk" not in kwargs:
            return JsonResponse(json)

        topic   = Topic.objects.filter(id=kwargs["pk"]).first()

        if not topic:
            return JsonResponse(json)

        topic.delete()

        context             = {}
        context["topics"]   = Topic.objects.all()

        json["error"]   = False
        json["content"] = render_to_string("bbs/content.html",context,request)

        return JsonResponse(json)

index   = IndexView.as_view()



