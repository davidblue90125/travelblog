from .models import Comment, Traveller
from django import forms
from django_summernote.widgets import SummernoteWidget
from cloudinary.forms import CloudinaryFileField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Traveller
        fields = ['bio', 'profile_image', 'fav_country', 'wishlist_country']
        widgets = {
            'bio': SummernoteWidget(),
            'profile_image': CloudinaryFileField().widget,
        }
        labels = {
            'bio': 'Biography (A few words about yourself)',
            'profile_image': 'Profile Picture',
            'fav_country': 'Favourite Country',
            'wishlist_country': 'Country you want to visit the most',
        }
