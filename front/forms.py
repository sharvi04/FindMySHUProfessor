from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from scms.models import Reply, Review, MemberProfile, StudentProfile

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['message']
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["subject", "rating", "review_description"]
        widgets = {
            "subject": forms.Select(attrs={"class": "form-select"}),  # Applying Bootstrap styling
            "rating": forms.Select(attrs={"class": "form-select"}),  # Consistent styling for dropdown
            "review_description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Write your review..."}),
        }
    def __init__(self, *args, **kwargs):
        professor = kwargs.pop("professor", None)  # Get professor from view
        super().__init__(*args, **kwargs)
        
        if professor:
            # Limit subject choices to the ones assigned to this professor
            self.fields["subject"].queryset = professor.subjects.all()
        
class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = [
            "profile_picture", "department", "designation",
            "contact_number", "office_address", "bio"
        ]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 3}),
        }
        
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['roll_number', 'course', 'year_of_study', 'contact_number', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super(StudentProfileForm, self).__init__(*args, **kwargs)

        # Apply Bootstrap styling to each field
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):  
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

        # Special styling for file input
        self.fields['profile_picture'].widget.attrs['class'] = 'form-control form-control-file'