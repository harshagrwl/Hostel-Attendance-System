from django.shortcuts import render

# Create your views here.
def stu_list(request):
	return render(request, 'stu/stu_list.html', {})