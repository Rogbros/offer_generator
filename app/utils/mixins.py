from django_htmx.http import HttpResponseClientRedirect


class HTMXSwapPartialMixin:
    partial_template_name: str = None

    def __init__(self):
        if self.partial_template_name is None:
            raise NotImplementedError("HTMXSwapPartialMixin error: `partial_template_name` not provided")
        super().__init__()

    def get_template_names(self):
        if self.request.htmx:
            return self.partial_template_name
        return self.template_name


class HTMXRedirectMixin:
    allow_htmx_redirect: bool = False

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if self.request.htmx and response.status_code in [301, 302] and not self.allow_htmx_redirect:
            return HttpResponseClientRedirect(response.url)

        return response
