from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label=u"Ulanyjy ady")
    first_name = forms.CharField(label=u"Ady")
    last_name = forms.CharField(label=u"Familiýa")
    email = forms.EmailField(label=u"Email", required=False)
    password = forms.CharField(label=u"Password", widget=forms.PasswordInput)
    password_confirm = forms.CharField(label=u"Password confirmation", widget=forms.PasswordInput)

    def is_valid(self):
        valid = super(RegisterForm, self).is_valid()
        if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
            self.add_error("password_confirm", u"Parollar gabat gelenak!")
            return False
        return valid

from Baglan.models import Profile, Post

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['user']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ['author']