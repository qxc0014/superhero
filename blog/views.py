from django.template.loader import get_template
from django.shortcuts import redirect 
from django.http import HttpResponse
from .models import BlogPost
from datetime import datetime


# Create your views here.
def homepage(request):
	template = get_template ('index.html')
	posts = BlogPost.objects.all()
	now = datetime.now()
	html = template.render(locals())
#	post_lists = list()
#	for count, post in enumerate(posts):
#		post_lists.append("No.{}:".format(str(count)) + str(post)+"<br>")
#		post_lists.append("<small>" + str(post.body.encode('utf-8'))  + "</small><br><br>")
        return HttpResponse(html)

def showpost(request, slug):
   template = get_template('post.html')
   try:
      post = BlogPost.objects.get(slug=slug)
      if post != None:
         html = template.render(locals())
         return HttpResponse(html)
   except:
       return redirect('/')
