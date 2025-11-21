from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loop through all fields and add dark theme styling classes
        for field in self.fields.values():
            field.widget.attrs['class'] = 'w-full p-3 rounded-md border border-gray-600 focus:outline-none focus:ring-2 focus:ring-green-400 bg-gray-700 text-gray-200 placeholder-gray-400'

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
        # Note: We've moved the widgets to the __init__ method for easier styling
