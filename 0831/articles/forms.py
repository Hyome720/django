from dataclasses import field
from re import A
from django import forms
from django import forms
from .models import articleModel

class ArticleForm(forms.ModelForm):
    name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': '내 이름',
                'placeholder': '이름을 입력하세요',
                'maxlength': 10,
            }
        ),
        error_messages={
            'required': '이름을 꼭 입력하세요'
        }
    )
    age = forms.IntegerField(
        label='나이',
        widget=forms.NumberInput(
            attrs={
                'placeholder': '나이를 입력하세요',
            }
        ),
        error_messages={
            'required': '나이를 꼭 입력하세요'
        }
    )
    
    class Meta:
        model = articleModel
        fields = '__all__'
