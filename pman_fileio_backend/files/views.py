
from rest_framework import generics, permissions

from core.renderers import BinaryFileRenderer

from .models import FileUpload
from .serializers import FileUploadSerializer


class FileUploadList(generics.ListCreateAPIView):
    """
    A view for the collection of files.
    """
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    permission_classes = (permissions.IsAuthenticated,)


class FileUploadDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A file's view.
    """
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    permission_classes = (permissions.IsAuthenticated)


class FileResource(generics.GenericAPIView):
    """
    A view to enable downloading of a file resource .
    """
    queryset = FileUpload.objects.all()
    renderer_classes = (BinaryFileRenderer,)
    permission_classes = (permissions.IsAuthenticated)

    def get(self, request, *args, **kwargs):
        """
        Overriden to be able to make a GET request to an actual file resource.
        """
        file = self.get_object()
        return Response(file.fname)
