from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    question_choices = [
        ('q1', 'Your favourite Name?'),
        ('q2', 'Your favourite Number?'),
        ('q3', 'Your favourite Thing?'),
    ]
    question = forms.ChoiceField(choices=question_choices, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    answer = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=51, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    role_choices = [
        ('seller', 'Seller'),
        ('buyer', 'Buyer'),
    ]
    role = forms.ChoiceField(choices=role_choices, required=True, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'question', 'role', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MyUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()

        MyUser.objects.create(
            user=user,
            question=self.cleaned_data['question'],
            answer=self.cleaned_data['answer'],
            city=self.cleaned_data['city'],
            role=self.cleaned_data['role']
        )
        return user

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password1')
        user = authenticate(email=email, password=password)
        if user is not None:
            raise forms.ValidationError('A user with that email already exists.')
        return cleaned_data
