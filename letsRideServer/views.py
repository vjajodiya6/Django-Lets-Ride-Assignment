from importlib.metadata import metadata
from urllib import request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from letsRideServer.models import Requests, Riders
from letsRideServer.serializers import RequestsSerializer, RidersSerializer



@csrf_exempt
def RequestsApi(request, emailId):
    if request.method == 'POST':
        requestData = JSONParser().parse(request)
        requests_serializer = RequestsSerializer(data=requestData)
        if requests_serializer.is_valid():
            requests_serializer.save()
            return JsonResponse(' Requets Added Successfully', safe=False)
        else:
            print(requests_serializer.is_valid())
            return JsonResponse('Failed to add requets', safe=False)
    elif request.method == 'GET':
        query_para = dict(request.GET)
        status_filter = query_para['status_filter'][0]
        asset_filter = query_para['asset_filter'][0]
        date_sort = query_para['date_sort'][0]
        query = 'SELECT * FROM letsRideServer_requests WHERE RequesterEmailid = "{mail}" '.format(mail=emailId)
        if len(asset_filter):
            query = query + ' AND Assettype = "{asset}"'.format(asset=asset_filter)
        if len(status_filter):
            query = query + ' AND Status = "{status}"'.format(status=status_filter)
        if (len(date_sort) and date_sort == 'True'):
            query = query + ' ORDER BY RequesterDate'
        asset_requests = Requests.objects.raw(query)
        requests_serializer = RequestsSerializer(asset_requests, many=True)
        return JsonResponse(requests_serializer.data, safe=False)



@csrf_exempt
def RiderApi(request, emailId):
    if request.method == 'POST':
        requestData = JSONParser().parse(request)
        rider_serializer = RidersSerializer(data=requestData)
        if rider_serializer.is_valid():
            rider_serializer.save()
            return JsonResponse(' Rider Added Successfully', safe=False)
        else:
            print(rider_serializer.is_valid())
            return JsonResponse('Failed to add Rider', safe=False)
    elif request.method == 'GET':
        asset_rider = Riders.objects.raw('SELECT * FROM letsRideServer_riders WHERE RiderEmailid = "{mail}"'.format(mail=emailId))
        rider_serializer = RidersSerializer(asset_rider, many=True)
        return JsonResponse(rider_serializer.data, safe=False)

@csrf_exempt
def matcher(request, emailId):
    if request.method == 'GET':
        query_para = dict(request.GET)
        page_no = query_para['page_no'][0]
        limit = query_para['limit'][0]
        offset = (int(page_no)-1)*int(limit)
        query = 'SELECT letsRideServer_requests.RequestId,letsRideServer_riders."RiderContact",letsRideServer_riders."From",letsRideServer_riders."To",letsRideServer_riders."RiderDate",letsRideServer_requests."TotalAssets",letsRideServer_requests."Assettype",letsRideServer_requests."Assetsensitivity", letsRideServer_requests."DeliveryContact", letsRideServer_requests."Status" FROM letsRideServer_requests INNER JOIN letsRideServer_riders WHERE letsRideServer_requests."RequesterEmailid" = "r1@gmail.com" AND letsRideServer_requests."From" = letsRideServer_riders."From" AND letsRideServer_requests."To" = letsRideServer_riders."To" AND letsRideServer_requests."RequesterDate" = letsRideServer_riders."RiderDate" LIMIT {limit} OFFSET {offset}'.format(mail=emailId,limit=limit,offset=offset)
        asset_requests = Requests.objects.raw(query)
        requests_serializer = RequestsSerializer(asset_requests, many=True)
        return JsonResponse(requests_serializer.data, safe=False)



