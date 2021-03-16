from django import forms
from .models import Resume

GENDER_CHOICES=[
  ('Male' ,'Male'),
  ('Female','Female')
]
JOB_CITY=[
  ('Mumbai','Mumbai'),
  ('Pune','Pune'),
  ('Bangalore','Bangalore'),
  ('Nagpur','Nagpur'),
  ('Kerla','Kerla')
]

class ResumeForm(forms.ModelForm):
  gender=forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
  job_city=forms.MultipleChoiceField(label='Preffered Job Locations', choices=JOB_CITY, widget=forms.CheckboxSelectMultiple)
  class Meta:
    model=Resume
    fields=['id','name','dob','gender','locality','city','pin','state','email','mobile','job_city','profile_image','my_file']
    labels = {'name':'Full Name', 'dob':'Date of Birth', 'gender':'Gender', 'locality':'Locality', 'city':'City', 'pin':'Pin Code', 'state':'State', 'email':'Email ID', 'mobile':'Mobile No.','job_city':'Job City', 'profile_image':'Profile Image','my_file':'My File'}
    widgets = {
      'name':forms.TextInput(attrs={'class':'form-control'} ),
      'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'} ),
      'gender':forms.TextInput(attrs={'class':'form-control'} ),
      'locality':forms.TextInput(attrs={'class':'form-control'} ),
      'city':forms.TextInput(attrs={'class':'form-control'} ),
      'pin':forms.NumberInput(attrs={'class':'form-control'} ),
      'state':forms.Select(attrs={'class':'form-select'} ),
      'email':forms.EmailInput(attrs={'class':'form-control'} ),
      'mobile':forms.NumberInput(attrs={'class':'form-control'} ),
      
    }