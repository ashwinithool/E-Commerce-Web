
from .models import Category, Product,Customer,Order
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.hashers import make_password,check_password

#from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q



# Create your views here.

class Index(View):

  def post(self,request):
    product=request.POST.get('product')
    remove=request.POST.get('remove')
    cart=request.session.get('cart')
    if cart:
      quantity=cart.get(product)
      if quantity:
        if remove:
          if quantity<=1:
            cart.pop(product)
          else:
            cart[product]=quantity-1
        else:
         cart[product]=quantity+1

      else:
        cart[product]=1
    else:
      cart={}
      cart[product]=1
    request.session['cart']=cart
    print('cart',request.session['cart'])
    return redirect('index')

  def get(self,request):
    cart=request.session.get('cart')
    if not cart:
      request.session['cart']={}
    #product={}
    product=None
    
    #categories={}
    categories=Category.objects.all()
     
   
    category_id=request.GET.get('category')
    if category_id:
        product=Product.objects.filter(category=category_id)
    else:
        product=Product.objects.all()
    data={}
    data['product']=product
    data['categories']=categories
    print('you are:',request.session.get('email'))
    
    return render(request,'index.html',data)
    #return render(request,'index.html',{'product':product})

def validateCustomer(customer):
  error_message=None
  if(not customer.first_name):
      error_message="First Name Required !!"
  elif len(customer.first_name) < 4:
      error_message="First name must be 4 char long"
  elif not customer.last_name:
      error_message="Last Name Required !!"
  elif len(customer.last_name) < 4:
      error_message="Last name must be 4 char long"
  elif not customer.phone:
      error_message="Phone no Required !!"
  elif len(customer.phone) < 10:
      error_message="Phone no must be 10 char long"
  elif not customer.password:
      error_message="Password Required !!"
  elif len(customer.password) < 6:
      error_message="Password must be 6 char long"
  elif len(customer.email) < 5:
      error_message="Email must be 5 char long"

  elif customer.isExists():
      error_message="Email Already Registered"
    
  return error_message

def registerUser(request):
    sm=request.POST
    first_name=sm.get('first_name')
    last_name=sm.get('last_name')
    phone=sm.get('phone')
    email=sm.get('email')
    password=sm.get('password')

    value={
      'first_name':first_name,'last_name':last_name,'phone':phone,'email':email

    }
    error_message=None

    customer=Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)
    error_message=validateCustomer(customer)

  #Save
    if not error_message:
      print(first_name,last_name,phone,email,password)
      customer.password=make_password(customer.password)
      
      customer.save()
      return redirect('/')
    else:
        data={
          'error':error_message,'values':value}
        return render(request,'signup.html',data)

def signup(request):
  if request.method=='GET':
    return render(request,'signup.html')
  else:
    return registerUser(request)

  
    
    
    #Validation

    


    
    
   

def user(email):
    return Customer.objects.filter(email=email)

def login(request):
  if request.method=='GET':
    return render(request,'login.html')
  else:
    lm=request.POST
    email=lm.get('email')
    password=lm.get('password')
    customer=Customer.objects.get(email=email)
    error_message=None
    if customer:
      flag=check_password(password,customer.password)
      if flag:
        request.session['customer']=customer.id
       
        return redirect('/')
      else:
        error_message="Email or passwaord Invalid"
    else:
      error_message="Email or passwaord Invalid"
    
    print(email,password)
    return render(request,'login.html',{'error':error_message})

  

def logout(request):
  request.session.clear()
  return render(request,'login.html')
  


def cart(request):
  if request.method=='GET':
    ids=list(request.session.get('cart').keys())
    product=Product.objects.filter(id__in=ids)
    print(product)
    return render(request,'cart.html',{'product':product})

#def checkout(request):
 # if request.method=='POST':
  #   address=request.POST.get('address')
   #  phone=request.POST.get('phone')
    # customer=request.session.get('customer')
     #cart=request.session.get('cart')
     #cart=request.session.get('cart')
     #print(address,phone,customer,cart,product)
     #return redirect('cart')///

class CheckOut(View):
  def post(self,request):
    address=request.POST.get('address')
    phone=request.POST.get('phone')
    customer=request.session.get('customer')
    cart=request.session.get('cart')
    ids=list(request.session.get('cart').keys())
    product=Product.objects.filter(id__in=ids)

    #product=Product.objects.get(list(cart.keys()))
    print(address,phone,customer,cart,product)

    
    #for product in product:
     # order=Order(customer=Customer(id=customer),product=product,
      #price=product.price,address=address,phone=phone,quantity=cart.get(product.id))
      #order.save()
      
      
     
    return redirect('cart')