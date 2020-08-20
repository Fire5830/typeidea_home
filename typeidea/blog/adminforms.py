from dal import autocomplete
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Category, Tags, Post


class PostAdminForms(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    # category = forms.ModelChoiceField(
    #     queryset=Category.objects.all(),
    #     widget=autocomplete.ModelSelect2(url='category-autocomplete'),
    #     label='分类',
    # )
    #
    # tag = forms.ModelMultipleChoiceField(
    #     queryset=Tags.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
    #     label='标签',
    # )

    content = forms.CharField(widget=CKEditorUploadingWidget(), label='内容', required=True)

    # class Meta:
    #     model = Post
    #     fields = ('category', 'tag', 'title', 'desc', 'content', 'status')
