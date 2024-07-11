from django.shortcuts import render, redirect, HttpResponse 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from.models import Order, OrderItem, Student, Book, Category
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from .models import Book,Cart




def index(request):
   

    category = request.GET.get('category')

    if category == None:
        books = Book.objects.all()
    else:
         books = Book.objects.filter(category__name=category)


    page_num = request.GET.get("page")

    paginator = Paginator(books, 6)

    try:
        books = paginator.page(page_num)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage():
        books = paginator.page(Paginator.num_pages)
    
    categories = Category.objects.all()

    context = {
        'books' : books,
        'categories' : categories
    }

    return render(request, 'index.html', context)
    #return HttpResponse("this is a homepage")


def searchbar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            books = Book.objects.filter(Q(author__icontains=query) | Q(title__icontains=query) | Q(isbn__icontains=query) | Q(publisher__icontains=query))
         
            return render(request, 'searchbar.html', {'books':books})
    
        else:
            print("no information to show")
            return render(request, 'searchbar.html', {})
 
def book_desc(request,pk):
    eachBook = Book.objects.get(id=pk)

    context = {
        'eachBook' : eachBook  
    }

    return render(request, 'book_desc.html',context)



def yourbook(request):
    return render(request, 'yourbook.html')

'''def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')
        student = Student.get_student_by_name(name)
        error_message = None
        if student:
            flag = check_password(password, student.password)
            if flag:
                request.session['student_id'] = student.id
                request.session['name'] = student.name
                return redirect('home')
            else:
                error_message = 'Inavlid name or password'
        else:
            error_message = 'Inavlid name or password'
        print(name,password)
        return render(request, 'login.html' ,{'error':error_message})'''
'''''
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        postDATA = request.POST
        name = postDATA.get('name')
        stud_id = postDATA.get('studentid')
        email = postDATA.get('email')
        password = postDATA.get('password')
        #validation
        value = {
            'name' : name,
            'stud_id' : stud_id,
            'email' : email
        }
        error_message = None
        student = Student(name=name,
                         stud_id=stud_id,
                         email=email,
                         password=password)
        if(not name):
            error_message = "Name required!"
        elif len(name) < 3:
            error_message = "name must be 3 character long"
        elif (not stud_id):
            error_message = "student id required"
        elif len(stud_id) < 5:
            error_message = "student id must be 5 char long"
        elif len(email) < 5:
            error_message = 'Email required'
        elif len(password) < 6:
            error_message = 'Password must be 6 char long'
        elif student.isExist():
            error_message = "Email Already Registered"
        
        #saving
        if not error_message:
            print(name , stud_id , email , password)
            student.password = make_password(student.password)
            student.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values' : value
            }
            return render(request, 'signin.html' , data)'''''


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
    messages.info(request,'Login failed, Try again')
    return render(request, 'user_login.html')


def user_register(request):
    if request.method  == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        stud_id = request.POST.get('stud_id')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
    
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
                return redirect('user_register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.info(request,'Email already exist')
                    return redirect('user_register')
                    
                    
                else:
                       if(not username):
                            messages.info(request,'name required')
                       elif len(email) < 5:
                            messages.info(request,'Email required')
                       elif (not stud_id):
                            messages.info(request,'Student ID Required')
                       elif len(stud_id) < 5:
                            messages.info(request,'Student ID Must be 5 char')
                       elif len(password) < 6:
                            messages.info(request,'Password must be 6 char long')
                
                       else:
                            user = User.objects.create_user(username=username,email=email,password=password)
                            user.save()
                            data = Student(user = user,stud_id=stud_id)
                            data.save()
    
                            our_user = authenticate(username=username,password=password)
                            if our_user is not None:
                                login(request,user)
                                return redirect('user_login')
        else:
            messages.info(request,'password is not matching')
            return redirect('user_register')
    return render(request, 'user_register.html')

    

def user_logout(request):
    logout(request)
    return redirect('home')
        
        
def add_to_cart(request,pk):
    book = Book.objects.get(pk=pk)

    order_item, created = OrderItem.objects.get_or_create(
        book=book,
        user=request.user,
        ordered=False,
    )
 
    order_qs = Order.objects.filter(user=request.user, items__ordered=False)
    if order_qs.exists():
        order = order_qs[0]  # Corrected variable name here
        if order.items.filter(book__pk = pk).exists():
            order_item.save()
            messages.info(request, "Added quantity item")
            return redirect("book_desc", pk=pk)
        else:
            order.items.add(order_item)
            messages.info(request, "Book added to cart")
            return redirect("book_desc", pk=pk)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Book added to cart")

        return redirect("book_desc",pk=pk)

def cart(request):
    if Order.objects.filter(user=request.user,ordered=False).exists():
        order = Order.objects.get(user = request.user,ordered=False)
        return render(request,'cart.html',{'order':order})
    return render(request,'cart.html',{'message':"No Books has been borrowed"})
    
