from django import forms
from .models import Report

SOCIAL_MEDIA_PLATFORMS = [
    ('Facebook', 'Facebook'),
    ('Instagram', 'Instagram'),
    ('LinkedIn', 'LinkedIn'),
    ('Snapchat', 'Snapcaht'),
    ('TikTok', 'TikTok'),
    ('Twitter/X', 'Twitter/X')
]

CATEGORIES = [
    ('Abuse', 'Abuse'),
    ('Scam', 'Scam')
]


class ReportForm(forms.ModelForm):
    social_media_platform = forms.ChoiceField(choices=SOCIAL_MEDIA_PLATFORMS)
    category = forms.ChoiceField(choices=CATEGORIES)

    class Meta:
        model = Report
        fields = [
            'social_media_platform',
            'social_media_handle',
            'category',
            'description'
        ]
