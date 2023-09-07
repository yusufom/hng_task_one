from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime

# Create your views here.
from rest_framework import renderers

class CustomRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = data
        return super().render(response_data, accepted_media_type, renderer_context)

class TaskView(APIView):
    renderer_classes = [CustomRenderer]

    def get(self, request):
        slack_name = request.GET.get('slack_name')
        track = request.GET.get('track')
        res = {
            "slack_name": slack_name,
            "current_day": datetime.now().strftime('%A'),
            "utc_time": datetime.now(),
            "track": track,
            "github_file_url": "https://github.com/yusufom/hng_task_one/blob/main/base/views.py",
            "github_repo_url": "https://github.com/yusufom/hng_task_one/",
            "status_code": status.HTTP_200_OK
            }
        return Response(res, status=status.HTTP_200_OK)