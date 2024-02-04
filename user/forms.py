from  django import forms

from  django.contrib.auth import get_user_model

User=get_user_model()
class UserEditForm(forms.ModelForm):
    
    
    #NOTE - UserForm is a form that allows users to update their profile information.
    #       It includes fields for picture, is_private_account, and phone_number.

    
    class Meta:
        
        model= User
        fields = (
            'picture',
            'full_name',
            'username',
            'email',
            'bio',
            'website',
            'phone_number',
            'gender',
            'is_private_account',
            )
        
         # Define the labels for the form fields.
         
        labels = {
            'is_private_account': 'Do you want to make your account private ?',
            'phone_number': 'Phone'
        }
    def __init__(self, *args, **kwargs):
        """
        Initialize the UserForm.
        Update the attributes of the form fields.
        """

        # Call the parent class's __init__ method.
        super().__init__(*args, **kwargs)

        # Iterate over each field in the form.
        for field in self.fields:

            # If the field is a picture, update its attributes.
            if field == 'picture':
                self.fields[field].widget.attrs.update({'class': 'form-control-file'})

            # If the field is is_private_account, update its attributes.
            elif field == 'is_private_account':
                self.fields[field].widget.attrs.update({'class': 'form-check-input'})

            # If the field is neither a picture nor is_private_account, update its attributes.
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control form-control-sm'})

