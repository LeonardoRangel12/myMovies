from django import forms
class ReviewsForm(forms.Form):
    movie_id = forms.IntegerField()
    rating = forms.IntegerField(min_value=1, max_value=100)
    review = forms.CharField(widget=forms.Textarea)