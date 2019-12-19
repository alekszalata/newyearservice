from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


@api_view(["GET"])
def daystillNY(request):
    try:
        if request.method == "GET":
            days = datetime(int(2020), 1, 1) - datetime.now()
            json_pack = JsonResponse(f"New {str(2020)} year will be in {str(days.days)} days", safe=False)
            return json_pack
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def daystillNY_byyear(request, data):
    try:
        if request.method == "GET":
            yeardata = int(data)
            print(f"YEARDATA IS {yeardata}")
            days = datetime(int(yeardata), 1, 1) - datetime.now()
            json_pack = JsonResponse(f"New {str(yeardata)} year will be in {str(days.days)} days", safe=False)
            return json_pack
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
