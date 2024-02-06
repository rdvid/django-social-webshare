from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from .models import Image
import requests


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widget = {
            'url': forms.HiddenInput
        }

    def clean_url(self):
        """
        subscribing clean field function for valid extension validation
        """
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1]
        if extension not in valid_extensions:
            raise forms.ValidationError('image has invalid format')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        """
        subscribing main save modelForm function for
        """
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        # download image from url
        response = requests.get(image_url)
        image.image.save(image_name,
                         ContentFile(response.content),
                         save=False)
        if commit:
            image.save()
        return image
