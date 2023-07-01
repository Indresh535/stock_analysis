from django import forms


class UploadedFileForm(forms.Form):
    title=forms.CharField(max_lenghth=50)
    file=forms.FileField