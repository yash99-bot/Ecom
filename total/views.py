from .models import product
from django.shortcuts import render , redirect, HttpResponseRedirect
from django.http import HttpResponse
from .models import customer
from django.contrib.auth.hashers import make_password, check_password
from django.views.generic import View
from totel.middleware.auth import auth_middleware
from django.utils.decorator import MiddlewareMixin




 #def index(request):
  #  products=product.objects.get
   # print(products)
    #return render(request, 'index.html', {'products' : products})
class Index(View):
    def get(self,request):
        products=product.objects.all()
        context = {'products':products}
        print('you are : ' , request.session.get('email'))
        return render(request,'index.html',context)

    def post(self,request):
        product = request.POST.get('product')
        cart = request.POST.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart   
        print('cart',request.session['cart'])
        return redirect('index')

class Signup(View):
    def get(self,request):
        return render(request,'signup.html')

    def post(self,request):
        postDate = request.POST
        first_name = postDate.get('firstname')
        last_name  = postDate.get('lastname')
        email  = postDate.get('email')
        password  = postDate.get('password')
        #validation
        error_massage = None
        customer = Customer(first_name=first_name,last_name=last_name,email=email,password=password)

        if (not first_name):
            error_message = "First name required!!"
        elif len(first_name) < 4:
            error_message = "First name must be 4 char long or more"
        
        elif (not last_name):
            error_message = "Last name required!!"
        elif len(last_name) < 4:
            error_message = "Last name must be 4 char long or more"

        elif (not email):
            error_message = "email required!!"
        
        elif (not password):
            error_message = "password name required!!"
        
        elif Customer.isExists():
            error_message = 'Email address already  registered..' 



     # saving
        if not error_message:
         print(first_name,last_name,email,password)
         customer.password = make_password(customer.password)     
         customer.save()
         return redirect(name='index')
        else:
            return render(request,'signup.html',{'error=error_message'})


    # staticmethod 
    def get_customer_by_email(email):
        try:
            return Customer.objects.filter(email = email)
        except:
            return False



class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request,'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = customer.get.customer.by.email(email)
        error_message = None
        if customer:
            flag= check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')    
                #return redirect(name='index')
            else:
                error_message = 'email or password invelid!!'
        else:
            error_message = 'email or password invelid!!'
            print(email,password)
            return render(request, 'login.html', {'error':error_message})
    
    def logout(request):
        request.session.clear()
        return redirect('login')


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = product.get_products_by_id(ids)
        print(products)
        return render(request,'cart.html' {'products': products})


class CheckOut(View):
    @auth_decorator(auth_middleware)
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart:keys())) 
        print(address,phone,customer,cart,products)
        
        for product in products:
            print(cart.get(str(product_id))) 
        order = Order(customer=Customer(id=customer),
        product = product,
        price = product.price,
        address = address,
        phone = phone)
        
        order.save()
        request.session['cart']={}

        print(order.placeorder());
        return redirect('cart')
 

class OrderView(View):
    def get(self,request)
    customer = request.session.get('customer')
    orders = order.get_orders_by_customer(customer)
    print(orders)
    return render(request, 'orders.html', {orders: 'orders'})

       
