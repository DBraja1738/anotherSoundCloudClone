from django import forms
from .models import Song

class SongUploadForm(forms.ModelForm):
    class Meta:
        model=Song
        fields=["title","artist","image","audio_file"]

class SongSearchForm(forms.Form):
    searchQuery=forms.CharField(label="Search for songs", max_length=100, required=False)

