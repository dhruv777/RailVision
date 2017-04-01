from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import cx_Oracle

# Create your views here.
#def search_form(request):
#   return render(request, 'search_form.html')
def dashboard(request):
	return render(request, "dashboard.html", {})

def home(request):
	return render(request, 'home.html',{})

def signup_confirm(request):
	return render(request, 'signup_confirm.html',{})	

def login(request):
	context = {}
	if(request.method == 'GET'):
		return render(request, "login.html" ,context)
	context = {"checked" : 0}

	if(request.method == 'POST'):
		connection = cx_Oracle.connect('dbms/dbms@localhost/orcl')
		user = request.POST.get("un")
		password = request.POST.get("pass")

		passwordFetchCursor = connection.cursor()
		passwordFetchCursor.execute('Select password from Person where username = \'' + user + '\'')
		returnedPass = None
		try:
			returnedPass = passwordFetchCursor.fetchone()[0]
		except:
			context = {"checked" : 1}	
		print returnedPass	
		passwordFetchCursor.close()
		connection.close()
		if(not returnedPass == None) and (password == returnedPass):
			print "madarchod"
			context = {"name" :user}
			#return redirect ('dashboard')
			return render(request, "Dashboard.html", context )
	return render(request, "login.html" ,context)		



def signup(request):

	#request is whenever you're changing contexts.
	#It contains information about get and post.

	#if(request.method == "POST"):
		#print request.POST

	#form = PersonForm(request.POST or None) #In case there's no information in the post data, don't send through the validator

	context={}

	if(request.method == 'GET'):
		return render(request,"signup.html",context)
	if(request.method == 'POST'):
		connection = cx_Oracle.connect('dbms/dbms@localhost/orcl')
		preloadUsersCursor = connection.cursor()
		preloadUsersCursor.execute('Select * from Person order by p_id desc')
		top = preloadUsersCursor.fetchone()[0]
		person_id = top+1
		print person_id
		user = request.POST.get("un")
		name = request.POST.get("name")
		mob_no = request.POST.get("phone")
		email = request.POST.get("email")
		gender = request.POST.get("gender")
		password = request.POST.get("password")
		print person_id
		newUser = [person_id, user, name, mob_no, email, gender, password]
		preloadUsersCursor.close()

		insertCursor = connection.cursor()

		insertCursor.execute('INSERT into person (p_id,username,name,mob_no, email, gender, password) values (:1, :2, :3, :4, :5, :6, :7)',newUser)
		connection.commit()
		insertCursor.close()

		context = {
			"template_title" : "Thanks for Signing Up !"
		}

		return render (request, "signup_confirm.html",context)	