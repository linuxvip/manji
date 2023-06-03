from rest_framework import renderers


class CustomJSONRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = {
            'code': renderer_context['response'].status_code,
            'message': renderer_context['response'].status_text,
            'data': data
        }
        return super().render(response_data, accepted_media_type, renderer_context)
