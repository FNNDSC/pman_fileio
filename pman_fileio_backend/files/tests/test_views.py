
import os, json, shutil

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.files import File
from django.contrib.auth.models import User
from django.conf import settings

from rest_framework import status

from files.models import FileUpload
from files import views


class ViewTests(TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

        

class FileUploadListViewTests(ViewTests):
    """
    Test the feed-list view
    """

    def setUp(self):
        super(FileUploadListViewTests, self).setUp()     
              
        self.list_url = reverse("fileupload-list")

    def test_fileupload_list_success(self):
        pass

    def test_fileupload_list_failure_unauthenticated(self):
        pass

        
