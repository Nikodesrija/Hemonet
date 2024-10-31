from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib import messages
from .models import BloodBank
from django.contrib.auth.models import User,auth
from .models import Donor 

def search_blood_banks(request):
    if request.method == 'POST':
        state = request.POST.get('state')
        district = request.POST.get('district')
        pincode = request.POST.get('pincode')
        blood_type = request.POST.get('blood_type')

        if blood_type not in dict(BloodBank.BLOOD_GROUP_CHOICES).keys():
            return render(request, 'search_form.html', {'error': 'Invalid blood type'})


        blood_banks = BloodBank.objects.filter(
            state=state,
            district=district,
            pincode=pincode,
            blood_type=blood_type,
        )

        return render(request, 'search_results.html', {'blood_banks': blood_banks})

    return render(request, 'search_form.html')

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def saveform(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        bloodgroup = request.POST.get('bloodgroup')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        district = request.POST.get('district')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        donation_date=request.POST.get('donation_date')
        donor = Donor(
            first_name=firstname,
            last_name=lastname,
            age=age,
            gender=gender,
            blood_group=bloodgroup,
            email=email,
            phone_number=phone,
            state=state,
            district=district,
            address=address,
            pincode=pincode,
            donation_date= donation_date,
        )
        donor.save()
        blood_banks = BloodBank.objects.filter(
            state=state,
            pincode=pincode,
        )
        return render(request, 'success.html', {'blood_banks': blood_banks})

    return render(request, 'register.html')

def success(request):
    return render(request, 'success.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'upload_blood.html')
        else:
            messages.info(request,'invalid credentials!!!')
            return redirect('loginpage')
    else:
        return render(request,'login.html')

def track_donation_status(request):
    donors = None
    error = None

    print(f"Request method: {request.method}")

    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        print(f"Phone number: {phone_number}")
        if phone_number:
            donors = Donor.objects.filter(phone_number=phone_number)
            if not donors:
                error = "*No records found for this phone number."
        else:
            error = "Please enter a valid phone number."

    print(f"Donors: {donors}, Error: {error}")
    return render(request, 'donation_status.html', {'donors': donors, 'error': error})

def upload_blood(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        state = request.POST.get('state')
        district = request.POST.get('district')
        pincode = request.POST.get('pincode')
        blood_type = request.POST.get('blood_type')
        blood_component = request.POST.get('blood_component')

        blood_bank = BloodBank(
            name=name,
            address=address,
            state=state,
            district=district,
            pincode=pincode,
            blood_type=blood_type,
            blood_component=blood_component
        )
        blood_bank.save()
        return redirect('succ')
    return render(request, 'upload_blood.html')

def succ(request):
    return render(request, 'succ.html')