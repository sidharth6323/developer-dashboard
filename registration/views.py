from django.shortcuts import render,HttpResponse,render_to_response,HttpResponseRedirect,RequestContext
from registration.models import registration
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from registration.serializers import registrationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
import json
from django.contrib.auth.models import User

def index(request):
	if request.method=="POST":
		user=User.objects.get(pk=1)
		token=Token.objects.get(user=user)
		client=APIClient()
		client.credentials(HTTP_AUTHORIZATION="Token "+token.key)
		client.post('/api/v1/register/', request.POST, format='json')
	return render_to_response("index.html",{},RequestContext(request))

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def register(request):
	if request.method=="POST":
		serializer=registrationSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return "registration successful"
		print serializer.errors
		return "Please fill all the forms appropriately"
		#return Response(serializer.errors) 