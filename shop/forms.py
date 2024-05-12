from django import forms
from .models import Contact, Review, Product
class ContactForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(label='Оберіть послугу/и, які Вас цікавлять:', queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone', 'email', 'products', 'comments']
        labels = {
            'first_name': "Ім'я:",
            'last_name': 'Прізвище:',
            'phone': 'Телефон:',
            'email': 'Електрона пошта:',
            'products': 'Оберіть послугу/и, які Вас цікавлять:',
            'comments': 'Залиште нам коментар чи своє запитання:'
        }


class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(label='Ваша оцінка', min_value=1, max_value=5)
    class Meta:
        model = Review
        fields = ['author', 'rating', 'text',]
        labels = {
            'author': "Ім'я:",
            'rating': 'Ваша оцінка:',
            'text': 'Ваш відгук:'
        }
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80}),
            'author': forms.TextInput(attrs={'placeholder': 'Your name'})
        }