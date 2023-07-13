from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm, CreateCampaignForm, PayementForm
from .models import Campaign
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def index(request):
    if request.user.is_authenticated:
        campaigns = Campaign.objects.all()
        x = Campaign.objects.get(id=1)
        donations = x.donations.all()
        print(donations)
        content = {"campaigns": campaigns}
        return render(request, "home.html", content)
    else:
        if request.method == 'GET':
            form = LoginForm()
            return render(request, 'index.html', {"form": form})
        elif request.method == 'POST':
            form = LoginForm(request.POST)
            
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request,username=username,password=password)
                if user:
                    login(request, user)
                    return redirect('/')
        # form is not valid or user is not authenticated

        return render(request,'index.html',{'form': form})
       
@login_required
def campaign(request):
    form = CreateCampaignForm()
    if request.method == "POST":
        form = CreateCampaignForm(request.POST, request.FILES)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.created_by = request.user
            campaign.save()
            return redirect("/")
    content = {"form": form}
    return render(request, 'campaign.html', content)
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('/')
        else:
            print(form.is_valid)
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
@login_required
def payment(request, slug):
    form = PayementForm()
    if request.method == "POST":
        form = PayementForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.campaign = Campaign.objects.get(slug=slug)
            donation.donor = request.user
            donation.transaction_id = "id"
            donation.save()
            return redirect("/")

    return render(request, 'payment.html', {"form":form })

def signout(request):
    logout(request)
    #messages.success(request,f'You have been logged out.')
    return redirect('/')     
