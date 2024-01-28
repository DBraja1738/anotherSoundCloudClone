from django import forms
from .models import Song

class SongUploadForm(forms.ModelForm):
    class Meta:
        model=Song
        fields=["title","artist","description","image","audio_file"]
        widgets = {
            "title": forms.TextInput(attrs={'size': '30'}),  
            "artist": forms.TextInput(attrs={'size': '30'}),  
        }
class SongSearchForm(forms.Form):
    searchQuery=forms.CharField(label="Search for songs", max_length=100, required=False)

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))

class RatingForm(forms.Form):
    rating = forms.IntegerField(min_value=1, max_value=5)
