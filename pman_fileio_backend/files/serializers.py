
import os

from rest_framework import serializers

from collectionjson.fields import ItemLinkField

from .models import FileUpload


class FileUploadSerializer(serializers.HyperlinkedModelSerializer):
    fname = serializers.FileField(use_url=False)
    file_resource = ItemLinkField('_get_file_link')

    class Meta:
        model = FileUpload
        fields = ('url', 'fname', 'file_resource')

    def _get_file_link(self, obj):
        """
        Custom method to get the hyperlink to the actual file resource
        """
        fields = self.fields.items()
        # get the current url
        url_field = [v for (k, v) in fields if k == 'url'][0]
        view = url_field.view_name
        request = self.context['request']
        format = self.context['format']
        url = url_field.get_url(obj, view, request, format)
        # return url = current url + file name
        return url + os.path.basename(obj.fname.name)
