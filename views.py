from django.shortcuts import render 
from food.forms import food_database1,food
from food.models import food_database
from django.http import HttpResponse


# Create your views here.


def index(response):
	return render(response,'base.html',{})
  
 
def index1(response):  

    if response.method == 'POST':
        data=food_database1(response.POST)
        data.save(commit=True)
        return render(response, 'base.html', {})

    else:
        food = food_database1()
        context={'w':food}
   
        return render(response,'base2.html',context)

def index2(response):
	return render(response,'base3.html',{})

def view_all(request): 
    context ={} 
    context["dataset"] = food_database.objects.all()      
    return render(request, "viewall.html", context)

def index3(response):
	if response.method=='POST':
		add_obj=food(response.POST)
		if add_obj.is_valid():
			lname = add_obj.cleaned_data['lname']
			a=food_database.objects.raw('SELECT * FROM food_food_database WHERE Enter_Location = %s', [lname])
			return render(response,'base5.html',{'data':a})

		else:
			return render(response,'base4.html',{'form':add_obj})

	else:
		add_obj= food()
		return render(response,'base4.html',{'form':add_obj})


def index4(response):
	return render(response,'base6.html',{})

def index5(response):
	return render(response,'base7.html',{})



	 






