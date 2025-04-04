from django import forms
from .models import SelectList, Category

class SelectListForm(forms.ModelForm):
    type = forms.ChoiceField(label='Type', choices=[])

    class Meta:
        model = SelectList
        fields = ['name', 'value', 'type', 'status', 'display_order']

    def __init__(self, *args, **kwargs):
        super(SelectListForm, self).__init__(*args, **kwargs)
        
        # Dynamically load choices for the 'type' field where status is 'active' and type is 'list'
        active_list_items = SelectList.objects.filter(type='LIST', status='active').order_by('display_order')

        # If there are items available, populate the 'type' field choices
        if active_list_items.exists():
            self.fields['type'].choices = [(item.value, item.name) for item in active_list_items]
        else:
            # If no active list items are available, set a default option
            self.fields['type'].choices = [('', 'No available options')]
            
            
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        # Dynamically load page layout choices from SelectList
        layouts = SelectList.objects.filter(type='LAYOUT', status='active')
        self.fields['page_layout'] = forms.ChoiceField(
            choices=[(layout.value, layout.name) for layout in layouts],
            widget=forms.Select(attrs={'class': 'form-control'})
        )