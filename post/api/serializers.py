from rest_framework import serializers

import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
IMAGE_SIZE_MAX_BYTES = 1024 * 1024 * 2 # 2MB
MIN_TITLE_LENGTH = 5
MIN_BODY_LENGTH = 50

# from blog.utils import is_image_aspect_ratio_valid, is_image_size_valid


class DetailsSerializer(serializers.ModelSerializer):

	class Meta :
		model = 