from uuid import uuid4
import requests
import os
from datetime import datetime

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView


class FileUploadSerializer(serializers.Serializer):
    """
    Serializer for uploading files.
    """
    files = serializers.ListField(child=serializers.FileField(max_length=100000, allow_empty_file=False, use_url=False))


def save_uploaded_files(uploaded_files, path):
    """
    Function to save uploaded files.

    :param uploaded_files: List of uploaded files
    :param path: Path to save files
    :return: List of saved file data
    """
    result_data = []

    for uploaded_file in uploaded_files:
        original_name = None
        extension = None
        url = None

        if isinstance(uploaded_file, str):
            # If a file URL is passed, download its content
            response = requests.get(uploaded_file)
            if response.status_code == 200:
                content_type = response.headers.get('content-type')
                extension = content_type.split('/')[-1] if content_type else ''
                new_name = f"{uuid4().hex}_{datetime.now().strftime('%Y%m%d%H%M%S')}{extension}"

                save_path = default_storage.save(os.path.join(path, new_name), ContentFile(response.content))
                url = default_storage.url(save_path)
        else:
            # If a file object is passed, save it
            original_name = uploaded_file.name
            extension = os.path.splitext(original_name)[-1].lower()
            new_name = f"{uuid4().hex}_{datetime.now().strftime('%Y%m%d%H%M%S')}{extension}"

            save_path = default_storage.save(os.path.join(path, new_name), uploaded_file)
            url = default_storage.url(save_path)

        file_data = {
            'file': url,
            'original_name': original_name,
            'extension': extension,
        }

        result_data.append(file_data)

    return result_data


class FileUploadView(APIView):
    """
    View for uploading files.
    """
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        uploaded_files = request.FILES.getlist('files')
        path = request.GET.get('path', 'uploads/')

        try:
            result_data = save_uploaded_files(uploaded_files, path)
            return Response(result_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
