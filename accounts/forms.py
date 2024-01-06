from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import validate_email

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"})
    )

    class Meta:
        model = User
        fields = ["email", "username"]

        # Add labels for each field
        labels = {
            "email": "Email",
            "username": "Username",
            "password": "Password",
        }

        # Use PasswordInput widget for the password field
        widgets = {
            "email": forms.TextInput(attrs={"placeholder": "e.g. guts@test.com"}),
            "username": forms.TextInput(attrs={"placeholder": "e.g. guts"}),
        }

    # def save(self, cleaned_data):
    #     email = cleaned_data.get("email")
    #     username = cleaned_data.get("username")
    #     password = cleaned_data.get("password")
    #     if not email or not username:
    #         raise ValueError("Email and username cannot be empty")

    #     try:
    #         user = User.objects.create_user(
    #             email=email,
    #             username=username,
    #             password=password,
    #         )
            
    #     except Exception as e:
    #         raise e

    #     return user


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={"placeholder": "Enter your email"}),
        required=True,
        help_text="Please enter an valid Email address",
        validators=[validate_email],
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"}),
        strip=False,
        required=True,
        help_text="Please enter the valide Password",
    )
