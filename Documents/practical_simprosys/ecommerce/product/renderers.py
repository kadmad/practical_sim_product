from django.utils.encoding import smart_str
from rest_framework import renderers
from cryptography.fernet import Fernet


class CustomRenderer(renderers.BaseRenderer):
    media_type = "text/plain"
    format = "txt"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        key = Fernet.generate_key()
        cipher = Fernet(key)
        key = cipher.generate_key()
        token = cipher.encrypt(str(data).encode())
        response = {"data": token, "key": key}
        return smart_str(response, encoding=self.charset)
