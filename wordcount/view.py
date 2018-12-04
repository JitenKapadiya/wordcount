from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
  return HttpResponse('<h1>This is Home Page</h1>')
  
def contact(request):
  return HttpResponse('<h1>This is Contact Page</h1>')
  
def service(request):
  return render(request,'service.html',{'name':'This is Nityam Webtech'})
  
def wordcal(request):
    return render(request,'wordcal.html')
  
def count(request):
  data = request.GET['t1']
  #print(data)
  word_list = data.split()
  #print(word_list)
  list_length = len(word_list)
  #print(list_length)
  
  wordictn = {}
  
  for word in word_list:
   if word in wordictn:
    wordictn[word] += 1
   else:
    wordictn[word] = 1
	
  sorted_list = sorted(wordictn.items(), key = operator.itemgetter(1), reverse = True)
		
  return render(request,'count.html', {'fulltext':data, 'words':list_length, 'worddictionary':sorted_list})