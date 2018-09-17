from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from random import randint
import datetime
from .models import *
login = 1
register = 2





# ========================= [ Index ]==============================
def index(request):
    errors =[]
    errors.append("Login failed , plese try again.")
    if 'id' not in request.session :
        context = {
        "errors" : errors,
        }
        return render(request,"BooksReview/index.html",context)
    else:
        return redirect("/books")

# ========================= [ Login ]==============================

def login(request):
    errors=validation(request,login)
    if len(errors)>0 :
        context = {
            # "users" : users.objects.all(),
            "errors" : errors
        }
        return render(request,"BooksReview/index.html",context)
    else:
        # ========= [ check password in database ]=============
        try:
            findData= users.objects.get(email__iexact=request.POST['email'],password=request.POST['password'])
        except:
            findData = ""


        if findData == "":
            err=[]
            err.append("Login failed")
            context = {
                "errors" : err
                }
            return render(request,"BooksReview/index.html",context)
        else:
            print "===========[ ok ]==========="
            request.session['id'] = findData.id
            return redirect("/books")

# ========================= [ Register ]==============================

def register(request):
    #=== [ Data Validation ]================
    errors=validation(request,register)
    if len(errors)>0 :
        context = {
            # "users" : users.objects.all(),
            "errors" : errors
        }
        return render(request,"BooksReview/index.html",context)
    else:
        #=== [  Validation : check if email is existed ]================
        try:
            findData= users.objects.get(email=request.POST['email'])
        except:
            findData = ""

        if not findData == "" :
            errors=[]
            errors.append("-------------[ Register failed ] -----------------")
            errors.append("Email is already existed! Please try register again")

            context = {
                "errors" : errors
            }
            return render(request,"BooksReview/index.html",context)


        #=== [  Validation : check if Login ]================
        try:
            findData= users.objects.get(email=request.POST['email'],password=request.POST['password'])

        except:
            findData = ""
            users.objects.create(name=request.POST['name'],alias=request.POST['alias'],email=request.POST['email'],password=request.POST['password'])

            findData= users.objects.get(email=request.POST['email'],password=request.POST['password'])
            request.session['id'] = findData.id
            return redirect("/books")
#
# # ========================= [ check login ]==============================
#
# def check_login(request):
#     #=== [  Validation : check if Login ]================
#     try:
#         findData= users.objects.get(email=request.POST['email'],password=request.POST['password'])
#     except:
#         findData = ""
#
#     if not findData == "" :
#         errors=[]
#         errors.append("-------------[ Login failed ] -----------------")
#         errors.append("Email is already existed! Please try register again")
#
#         context = {
#             "errors" : errors
#         }
#     return context
# ========================= [ Books Page ]==============================
def books(request):
    # if not len(errors)>0:
    #     errors =[]
    if 'id' not in request.session :
        errors.append("Login failed , plese try again.")
        context = {
        "errors" : errors,
        }
        return redirect("/",context)
    else:
        try:
            findData= users.objects.get(id=request.session['id'])
        except:
            findData = ""
        Reviews_list=review.objects.all()
        all_books_list =mybooks.objects.all()
        # Books_list=mybooks.objects.all().order_by('-created_at')
        Books_list=mybooks.objects.all().order_by('-created_at')[:5]
        users_list=users.objects.all()
        context = {
        "message" : "Successfully registered",
        "alias"  : findData.alias,
        "reviews_all": Reviews_list,
        "books_list":Books_list,
        "all_books_list":all_books_list,
        "users_list":users_list,
        }

        return render(request,"BooksReview/books.html",context )
# ========================= [ Review List ]==============================
    # url(r'^books/(?P<book_id>[0-9]+)$', views.reviewList),

def reviewList(request,book_id):


    if 'id' not in request.session :
        errors =[]
        errors.append("Login failed , plese try again.")
        context = {
        "errors" : errors,
        }
        return redirect("/",context)
    else:
        try:
            findData= users.objects.get(id=request.session['id'])
        except:
            findData = ""
        Reviews_list=review.objects.filter(curr_book_id=book_id)
        Books_list=mybooks.objects.get(id=book_id)
        users_list=users.objects.all()

        context = {
        "alias"  : findData.alias,
        "reviews_all": Reviews_list,
        "books_list":Books_list,
        "users_list":users_list,
        }
    return render(request,"BooksReview/reviewList.html",context )


# ========================= [ User profile]==============================
def user(request,user_id):
    u=users.objects.get(id=user_id)
    v=review.objects.filter(curr_user_id=user_id).order_by('curr_book_id')
            # Books_list=mybooks.objects.all().order_by('-created_at')

    vb = review.objects.raw("select * from BooksReview_review where curr_user_id=%s group by curr_book_id",[user_id])
    # +' group by curr_book_id order by curr_book_id')
    # vb=review.objects.filter(curr_user_id=user_id).group_by('curr_book_id')
    b = mybooks.objects.all()

    # print v
    total = len(v)

    # print total
    context ={
        'users' : u,
        'books' : b,
        'reviews' : v,
        'reviewsBooks' : vb,
        'total' : total
    }
    return render(request,"BooksReview/user.html",context )



# ========================= [ Delete Review]==============================
def deleteReview(request,review_id,book_id):
    # ================= [ Delete Review ]========================
    getData=review.objects.get(id=review_id)
    getData.delete()
    return redirect("/books/"+book_id)



# ========================= [ Add Books]==============================
def addBook(request):
    if 'id' not in request.session :
        context = {
        "errors" : "Session expired , plese loign.",
        }
        return redirect("/",context)
    else:
        try:
            findData= users.objects.get(id=request.session['id'])
        except:
            findData = ""
            context = {
            "errors" : "Session expired , plese loign.",
            }
            return redirect("/",context)
        try:
            author_list= mybooks.objects.raw("select * from BooksReview_mybooks group by author")
        except:
            author_list="non"

        context = {
        "name"  :   findData.name,
        "email" : findData.email,
        "alias"  : findData.alias,
        "author_list" : author_list
        }
    return render(request,"BooksReview/add.html",context)

#========================== [ Add Review process ]=================================
def add_review(request):

    this_user=users.objects.get(id=request.session['id'])
    this_book=mybooks.objects.get(id=request.POST['book_id'])
    this_book.all_users.add(this_user)
    review.objects.create(rate=request.POST['rate'],review=request.POST['review'],curr_book_id=this_book.id,curr_user_id=request.session['id'])
    this_review=review.objects.last()
    this_review.all_users.add(this_user)
    return redirect("/books/"+request.POST['book_id'])

#========================== [ Add Book and Review process ]=================================
def add(request):
    if not request.POST['author_list']== "" :
        Author = request.POST['author_list']
    else:
        Author = request.POST['author']

    mybooks.objects.create(author=Author,name=request.POST['title'],curr_user_id=request.session['id'])

    this_user=users.objects.get(id=request.session['id'])
    this_book=mybooks.objects.last()
    this_book.all_users.add(this_user)
    review.objects.create(rate=request.POST['rate'],review=request.POST['review'],curr_book_id=this_book.id,curr_user_id=request.session['id'])
    this_review=review.objects.last()
    this_review.all_users.add(this_user)
    return redirect("/books")

# ========================= [ Logout]==============================
def logout(request):
    request.session.clear()
    return redirect('/')

# ========================= [ Digit Validation ]==============================

def hasNumbers(inputString):
                        # return trun / false
    return any(char.isdigit() for char in inputString)

# ========================= [ Validation ]==============================

def validation(request,switch):
    if switch == register:
        errors =[]

        if len(request.POST['name']) < 2:
            errors.append("Name cannot be less than 2 characters;")

        # if not request.POST['name'].isalpha():
        #     errors.append("Name - Error : letters only")
        #
        # if hasNumbers(request.POST['first_name']):
        #     errors.append("First Name - Error : letters only ( Number should not included)")

        # ========= [ for Validation check char only (not num and sysbol)]=============

        if len(request.POST['alias']) < 1:
            errors.append("Alias cannot be empty;")

        if len(request.POST['email']) < 3:
            errors.append("Email format invalid - less than 3 characters")

        if not '@' in request.POST['email']:
            errors.append("Email format invalid - without @")

        if len(request.POST['password']) < 8:
            errors.append("Password invalid : at least 8 characters")

        if not request.POST['password'] == request.POST['re-password']:
            errors.append("Password Confirmation doesn't match ")

        return errors
    elif switch == login:
        errors = []
        return errors
# ========================= [ End ]==============================
