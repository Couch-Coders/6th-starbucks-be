from __future__ import annotations
from typing import TYPE_CHECKING

from django.shortcuts import redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import views
from rest_framework.response import Response
from loguru import logger

if TYPE_CHECKING:
    from django.http.request import HttpRequest
    from rest_framework.request import Request


class LogInView(views.APIView):
    def post(self, request: Request):
        logger.debug(request.data)
        return Response()


class LogOutView(views.APIView):
    def post(self, request: Request):
        return Response()
