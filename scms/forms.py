from django import forms
from django.contrib import admin
from .models import Page, JobRequest, Gallery, GalleryMedia
from user.models import Member
from django_summernote.widgets import SummernoteWidget
from setup.models import SelectList

class MemberForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'role', 'email', 'mobile', 'phone', 'whatsapp', 'city', 'state', 'country', 'zipcode', 'password', 'confirm_password', 'notes']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")




class PageForm(forms.ModelForm):
    
    class Meta:
        model = Page
        fields = '__all__'  # Include all fields from the model
        widgets = {
            'rich_intro': SummernoteWidget(), 
            'rich_body': SummernoteWidget(), 
        }
        

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        # Dynamically load choices for page_type from SelectList where type='PAGETYPE'
        self.fields['page_type'].choices = [
            (item.value, item.value) for item in SelectList.objects.filter(type='PAGETYPE')
        ]
        
        self.fields['group'].choices = [
            (item.value, item.value) for item in SelectList.objects.filter(type='GROUP')
        ]
        
        self.fields['content_access_level'].choices = [
            (item.value, item.value) for item in SelectList.objects.filter(type='CONTENTACCESS')
        ]
        

class JobRequestForm(forms.ModelForm):
    class Meta:
        model = JobRequest
        fields = ['name', 'phone', 'email', 'apply_role', 'resume', 'message']
        
        
class GalleryMediaForm(forms.ModelForm):
    class Meta:
        model = GalleryMedia
        fields = ['image', 'caption'] 