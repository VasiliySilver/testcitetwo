from django import forms
from .models import News

# ниже форма связанная с моделями

class NewsForm(forms.ModelForm):
    class Meta:
        """можно использовать __all__ чтобы добавить сразу все поля, create_at и updated_at заполняются автоматически"""
        model = News
        # fields = '__all__'  # здесь указываются поля в нашей форме
        # лучше описать явно поля
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }




































# class NewsForm(forms.Form):
    # title = forms.CharField(
    #     max_length=150,
    #     label='Название',
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control"
    #     }))
    # content = forms.CharField(
    #     label='Текст',
    #     required=False,
    #     widget=forms.Textarea(attrs={
    #     "class": "form-control",
    #     "rows": 5,
    # }))
    # is_published = forms.BooleanField(label='Опубликовано', initial=True)
    # category = forms.ModelChoiceField(
    #     queryset=Category.objects.all(),
    #     label='Категории',
    #     empty_label='Выберете категорию',
    #     widget=forms.Select(
    #         attrs={
    #             "class": "form-control"
    #         }))
