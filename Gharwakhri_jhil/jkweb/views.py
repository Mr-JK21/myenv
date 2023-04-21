from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import registery
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from accounts.forms import MyUserCreationForm
# from products.forms import ProductAdminForm
from catalog.models import Product, Order
from django.db.models import Max, F
#--------------------------------------------------------------------------------
from catalog.forms import OrderForm
from django.contrib import messages
from datetime import date

from catalog.forms import SubscribeForm
from django.urls import reverse
from pprint import pprint

from catalog.forms import ProductForm

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('catalog:create_product')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})

@login_required
def vendor_list(request):
    # sellers = User.objects.filter(groups__name='seller')
    sellers = User.objects.filter(registery__role='seller')

    context = {'sellers': sellers}
    print(context)
    return render(request, 'buyer/vendor_list.html', context)

def search(request):
    query = request.GET.get('q')
    try:
        products = Product.objects.filter(name__icontains=query)
        context = {'query': query, 'products': products}
        print(context)
    except Product.DoesNotExist:
        print(f"No products found with name containing '{query}'")
        context = {'query': query, 'products': []}
    return render(request, 'index-3.html', context)

@login_required
def only(request):
    order = Order.objects.filter(user=request.user)
    
    context = {'order': order}
    print(order)
    return render(request, 'only.html', context)

@login_required
def deactivate_account(request):
    if request.method == 'POST':
        # deactivate the user's account and log them out
        request.user.delete()
        logout(request)
        return redirect('home')
    return render(request, 'authenticate/deactivate.html')

def order_action(request, pk):
    order = Order.objects.get(pk=pk)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'confirm':
            order.status = 'Confirmed'
            order.save()
            messages.success(request, 'Order confirmed successfully!')
            return redirect('seller_order')
        elif action == 'reject':
            order.status = 'Rejected'
            order.save()
            messages.success(request, 'Order rejected successfully!')
            return redirect('seller_order')
        elif action == 'ready':
            order.status = 'Ready'
            order.save()
            messages.success(request, 'Order Ready For Pickup !')
            return redirect('seller_order')
    
    context = {'order': order}
    return render(request, 'order-s.html', context)


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('sellerhome')
    
    context = {'product': product}
    return render(request, 'seller/delete-product.html', context)

@login_required(login_url='/login/')
def seller_order(request):
    user = request.user
    products = Product.objects.filter(user=user).values()
    product_list=[]
    for i in products:
        product_list.append(
            i["id"]
        )
        # print(i)
    # print(product_list)
    order_list=Order.objects.filter(product_id__in=product_list)
    # print(order_list)
    return render(request, 'order-s.html', {'orders': order_list})

def cancel_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if order.status == 'Pending':
        order.delete()
        messages.success(request, 'Your order has been cancelled.')
    else:
        messages.warning(request, 'You cannot cancel this order.')
    return redirect('orderpage')

def subscribe(request):
    if request.method == 'POST':
        frn = SubscribeForm(request.POST)
        if frn.is_valid():
            email = frn.cleaned_data['email']
            return redirect('home')
    else:
        frn = SubscribeForm()
    return render(request, 'index-3.html', {'frn': frn})

@login_required
def buyer_order(request):
    if request.method == 'POST':
        print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            # Get the product and user from the form and request objects
            product_id = form.cleaned_data['product_id']
            product = Product.objects.get(pk=product_id)
            user = request.user
            
            # seller_name = product.seller.registery.user.username
            # seller_name = product.user.registery.username
            
            # Get the price and quantity from the form data
            quantity = form.cleaned_data['quantity']
            price = product.price
            # Calculate the total
            total = price * quantity
            # Create a new Order object and save it to the database
            order = Order.objects.create(
                user=user,
                product=product,
                price=price,
                quantity=quantity,
                total=total,
                status='Pending',
                # seller_name=seller_name
            )
            messages.success(request, 'Your order has been placed successfully!')
            return redirect('orderpage')
        else:
            messages.warning(request, 'Invalid form data!')
            product_id = form.cleaned_data['id']
            return redirect('product_detail', id=product_id)
    else:
        messages.warning(request, 'Invalid request method!')
        return redirect('product_detail')


def sdetails(request, sid):
    
    reg = registery.objects.get(user=sid)
    print(reg)
    phone_number = reg.phone_number
    username = request.user.username
    email = request.user.email
    city = reg.city
    print(reg)
    products = Product.objects.filter(user=sid)
    data = {
        'username': username,
        'email': email,
        'phone_number': phone_number,
        'city': city,
        'products': products,
    }
    print(username)
    #return render(request, 'sdetails.html', {'data': data})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    form = OrderForm(initial={'product_id': product.id})
    context = {'product': product, 'form': form}
    pprint(context)
    return render(request, 'product-detail.html', context)

def productdetail(request, id):
    # product = get_object_or_404(Product, id=id)
    product = Product.objects.get(pk=id)
    form = OrderForm(initial={'id': id})

    if 'message' in request.session:
        # get the message from the session and delete it
        message = request.session.pop('message')
    else:
        message = None
    
    return render(request, 'product-detail.html', {'product': product, 'form': form, 'message': message})
    # return render(request, 'product-detail.html', {'product': product})
    
@login_required
def orderpage(request):
    current_date = date.today()
    orders = Order.objects.filter(user_id=request.user).order_by('-id')
    order_list = []
    for order in orders:
        product = Product.objects.get(id=order.product_id)
        print(product.name)
        order_dict = {
            'id': order.id,
            'user_id': order.user_id,
            'name': product.name,
            'price': order.price,
            'quantity': order.quantity,
            'status': order.status,
            'date': current_date
        }
        order_list.append(order_dict)
    context = {
        'orders': order_list
    }
    return render(request, 'order-b.html', context)

def file_not_found_404(request, exception):
    page_title = 'Page Not Found'
    return render(request, 'page-404.html', {'page_title': page_title})

def home(request):
    cat = request.GET.get('category')
    
    # First, get the subquery for selecting the last product for each user
    last_products = Product.objects.filter(
        is_active=True,
    ).select_related('user').annotate(
        max_created_at=Max('created_at'),
    ).filter(
        created_at=F('max_created_at'),
    ).values('id')

    # Then, get the products by grouping by user and selecting the last product for each user
    lastadd = Product.objects.filter(
        id__in=last_products,
    ).order_by('-created_at').values(
        'id',
        'name',
        'image',
        'price',
        'selling_price',
        'user__username',
    )[:4]
    
    lastadd = {'lastadd': list(lastadd)}
    
    products = Product.objects.filter(is_active=True).order_by('-created_at')
    if cat:
        products = Product.objects.filter(categories=cat)
    # else:
    #     products = Product.objects.all()
        
    context = {'products': []}
    for product in products:
        context['products'].append({
            'name': product.name,
            'image': product.image,
            'price': product.price,
            'selling_price': product.selling_price,
            'user': product.user.username,  # Get the username of the user associated with the product
            'uid': product.user_id,
            'id': product.pk,
            'sid': product.user.id,
        })
    context.update(lastadd)
    pprint(lastadd)
    current_user = request.user
    if not current_user.is_authenticated:
        return render(request, 'index-3.html', context)

    try:
        registry = registery.objects.get(user=current_user)
    except registery.DoesNotExist:
        return render(request, 'index-3.html', context)

    if registry.role == 'seller':
        return redirect('sellerhome')

    return render(request, 'index-3.html', context)


def signup(request):
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            user = User.objects.create_user(
                username=request.POST.get('username'),
                password=password1,
                email=request.POST.get('email'),
            )
            user.save()
            phone=request.POST.get('phoneno')
            city=request.POST.get('city')
            question=request.POST.get('question')
            answer=request.POST.get('answer')
            role=request.POST.get('role')

            # Redirect the user to a success page or login page
            sv = registery(phone_number=phone,city=city,question=question,answer=answer,role=role,user=user)
            sv.save()
            # login user
            login(request, user)
            registration = registery.objects.get(user=user)
            role = registration.role
            if role=='seller':
                return redirect('sellerhome')
            else:
                return redirect('home') 

        else:
            # Add an error message to the context dictionary
            error_message = 'Passwords do not match'
            context = {'error_message': error_message}
            return render(request, 'authenticate/page-register.html',context)


    else:
        return render(request, 'authenticate/page-register.html')


def loginin(request):
    # clear current session
    request.session.flush()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Check if the user is a superuser
            if user.is_superuser:
                return redirect(reverse('admin:index'))
            
            # Get the user's role from the registration table
            try:
                registration = registery.objects.get(user=user)
                role = registration.role
                
                if role == 'seller':
                    return redirect('sellerhome')
                else:
                    return redirect('home')
                
            except registery.DoesNotExist:
                print("Registration not found for user: ", user)
                context = {'error': 'Invalid login credentials'}
                return render(request, 'authenticate/page-login.html', context)
            
        else:
            print("Invalid login credentials")
            context = {'error': 'Invalid login credentials'}
            return render(request, 'authenticate/page-login.html', context)
        
    else:
        return render(request, 'authenticate/page-login.html')


# def loginin(request):
#     # clear current session
#     request.session.flush()
    
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             # Get the user's role from the registration table
#             try:
#                 registration = registery.objects.get(user=user)
#                 role = registration.role
                
#                 if role == 'seller':
#                     return redirect('sellerhome')
#                 else:
#                     return redirect('home')
                
#             except registery.DoesNotExist:
#                 print("Registration not found for user: ", user)
#                 context = {'error': 'Invalid login credentials'}
#                 return render(request, 'authenticate/page-login.html', context)
            
#         else:
#             print("Invalid login credentials")
#             context = {'error': 'Invalid login credentials'}
#             return render(request, 'authenticate/page-login.html', context)
        
#     else:
#         return render(request, 'authenticate/page-login.html')
    

def logout(request):
    # clear current session
    request.session.flush()
    return redirect('home')


def sellerhome(request):
    if request.method != 'POST':
        # get the current logged in user
        reg = registery.objects.get(user=request.user)
        phone_number = reg.phone_number
        username = request.user.username
        email = request.user.email
        city = reg.city
        
        products = Product.objects.filter(user=request.user, is_active=True)
        data = {
            
            'username': username,
            'email': email,
            'phone_number': phone_number,
            'city': city,
            'products': products,
        }
        print(username)
        return render(request, 'seller/seller-home.html', {'data': data})
    return render(request, 'add_product.html')


def pgabout(request):
    return render(request, 'buyer/page-about.html')

#27th march 2:06 pm
def sellerprofile(request):
    if request.method != 'POST':
        # get the current logged in user
        reg = registery.objects.get(user=request.user)
        phone_number = reg.phone_number
        username = request.user.username
        email = request.user.email
        city = reg.city
        
        data = {
            'username': username,
            'email': email,
            'phone_number': phone_number,
            'city': city,
        }
        print(username)
        return render(request, 'seller-profile.html', {'data': data})
    return render(request, 'seller/seller-home.html')


def buyerhome(request):
    return render(request,'buyer/buyer-home.html')

def pgaccount(request):
    return render(request, 'page-account.html')

def pgcontact(request):
    return render(request, 'page-contact.html')



def privatepolicy(request):
    products = Product.objects.filter(is_active=True).order_by('-created_at')[:5]
    context = {'products': []}
    for product in products:
        context['products'].append({
            'name': product.name,
            'image': product.image,
            'price': product.price,            
        })
    return render(request, 'buyer/page-privacy-policy.html',context)

def purchaseguide(request):
    products = Product.objects.filter(is_active=True).order_by('-created_at')[:5]
    context = {'products': []}
    for product in products:
        context['products'].append({
            'name': product.name,
            'image': product.image,
            'price': product.price,            
        })
    return render(request, 'buyer/page-purchase-guide.html',context)

def pgterms(request):
    return render(request, 'buyer/page-terms.html')

def helpcenter(request):
    return render(request, 'seller/helpcenter.html')







