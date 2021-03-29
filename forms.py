from django import forms 
from food.models import food_database
  
# create a ModelForm 

class food_database1(forms.ModelForm): 
    
    class Meta: 
        model = food_database 
        fields = "__all__"


from django import forms

class food(forms.Form):
	lname=forms.CharField(label="Enter the Location?")
	



