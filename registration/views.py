from django.shortcuts import render,HttpResponse,render_to_response,HttpResponseRedirect,RequestContext
from registration.models import registration

def index(request):
	if request.method=="POST":
		f_name=request.POST.get("f_name")
		l_name=request.POST.get("l_name")
		gender=request.POST.get("gender")
		github=request.POST.get("github")
		course=request.POST.get("course")
		email=request.POST.get("email")
		usn=request.POST.get("usn")
		mobile=request.POST.get("mobile")
		year=request.POST.get("year")
		branch=request.POST.get("branch")
		registration.objects.create(f_name=f_name,l_name=l_name,gender=gender,github=github,course=course,email=email,usn=usn,mobile=mobile,year=year,branch=branch)
	return render_to_response("index.html",{},RequestContext(request))