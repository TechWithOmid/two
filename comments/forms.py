from django import forms
from django.utils.translation import ugettext_lazy as _

from django_comments_xtd.forms import XtdCommentForm
from django_comments_xtd.models import TmpXtdComment


class CommentForm(XtdCommentForm):
    """Customized comment form for django comment xtd"""
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = _("نام")
        self.fields['name'].widget = forms.TextInput(
            attrs={'placeholder': _('نام (الزامی)'), 'class': 'form-control'})
        self.fields['email'].label = _("ایمیل")
        self.fields['email'].help_text = _(" ")
        self.fields['email'].widget = forms.TextInput(
            attrs={'placeholder': _('آدرس ایمیل (الزامی'), 'class': 'form-control'})

        self.fields['url'].label = _("وبسایت")
        self.fields['url'].required = False
        self.fields['url'].widget = forms.TextInput(attrs={
                'placeholder': _('آدرس وبسایت شما (اختیاری)'),
                'class': 'form-control'})

        self.fields['comment'].widget = forms.Textarea(
            attrs={'placeholder': _('کامنت شما'), 'class': 'form-control', 'style': 'height: 100px;'})
