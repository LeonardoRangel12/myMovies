from django import forms
class ReviewsForm(forms.Form):
    movie_id = forms.IntegerField()
    rating = forms.IntegerField(min_value=1, max_value=100)
    review = forms.CharField(widget=forms.Textarea)
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)