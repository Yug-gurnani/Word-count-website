from django.http import HttpResponse
from django.shortcuts import render
def home(request):
	return render(request,"home.html")
def count(request):
	fulltext = request.GET['fulltext']
	wordlist = request.GET["fulltext"].split()
	dic = {"" : 0}
	for i in wordlist:
		if i not in dic:
			dic[i] = 1
		else:
			dic[i] += 1
	return render(request,"count.html",{'wordlist':fulltext, "len" : len(wordlist),'max': "{}: It appeared {} times".format(max(dic),dic[max(dic)])})

def about(request):
	return render(request,'about.html')