class HTMXSwapPartialMixin:
    partial_template_name: str = None

    def __init__(self):
        if self.partial_template_name is None:
            raise NotImplementedError("HTMXSwapPartialMixin error: `partial_template_name` not provided")
        super().__init__()

    def get_template_names(self):
        # if self.request.htmx:
        #     return self.partial_template_name
        return self.template_name
