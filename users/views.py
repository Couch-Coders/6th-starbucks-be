from __future__ import annotations
from typing import TYPE_CHECKING

from django.shortcuts import redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

if TYPE_CHECKING:
    from django.http.request import HttpRequest


def index(request: HttpRequest):
    return HttpResponse('index')