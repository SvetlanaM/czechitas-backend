from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields.pop('password2')
        self.fields['username'].required = False
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'



    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = False)
    last_name = forms.CharField(required = False)



    class Meta:
        model = User
        fields = ('first_name' , 'last_name', 'username', 'email', 'password1',
        )


    def save(self, commit = True):
        user = super(UserCreationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        pass1 = self.cleaned_data['password1']
        #pass2 = self.cleaned_data['password2']
        if pass1:
            user.password = pass1
        else:
            user.password = "Encoder+237"
        try:
            name = user.email
            temp_list = []
            for i in name:
                if i == "@":
                    break
                else:
                    temp_list.append(i)
            new_name = "".join(temp_list)
            user.username = new_name
        except forms.ValidationError("Username exists!"):
            name = user.email
            temp_list = []
            for i in name:
                if i == "@":
                    break
                else:
                    temp_list.append(i)
            new_name = "".join(temp_list)
            user.username = new_name[1:4]

        if commit:
            user.save()
        return user
