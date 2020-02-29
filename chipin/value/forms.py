from django import forms


class ValueChoiceForm(forms.Form):
    CHOICES = (
        ('World Hunger', 'World Hunger'),
        ('Climate Change', 'Climate Change'),
        ('Disease', 'Disease'),
        ('Wild Life Preservation', 'Wilf Life Preservatioon'),
        ('Government Accountability', 'Government Accountability'),
    )
    value = forms.ChoiceField(choices=CHOICES)
    
  
  

