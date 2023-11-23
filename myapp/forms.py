from django import forms
from myapp.models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
    
        widgets={
            'Rollno':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Rollnumber'}),
            'Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Name'}),
            'Class':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Class'}),
            'Gender':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Gender'}),
            'Age':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Age'}),
            'Group':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Group'}),
            'Address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Address'})
        }