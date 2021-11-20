from django import forms 

class PeopleForm(forms.ModelForm):
  class Meta:
    model = People
    widgets = {
   'pwd': forms.PasswordInput(),
}