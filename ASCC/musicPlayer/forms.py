from django import forms
from .models import Song
from django.core.exceptions import ValidationError

class SongUploadForm(forms.ModelForm):
    class Meta:
        model=Song
        fields=["title","artist","description","image","audio_file"]
        widgets = {
            "title": forms.TextInput(attrs={'size': '30'}),  
            "artist": forms.TextInput(attrs={'size': '30'}),  
            
        }

    def clean_audio_file(self):
        audio_file=self.cleaned_data.get("audio_file")

        if audio_file:
            if not audio_file.name.endswith(".mp3"):
                raise ValidationError("Only mp3 files are allowed")
        return audio_file
    


class SongSearchForm(forms.Form):
    searchQuery=forms.CharField(label="Search for songs", max_length=100, required=False)

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))


