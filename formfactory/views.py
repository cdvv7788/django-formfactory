from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views import generic

from formfactory.models import Form


class FactoryFormView(generic.FormView):
    template_name = "formfactory/form_detail.html"

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request, messages.SUCCESS, self.form_object.success_message
        )
        return super(FactoryFormView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR, self.form_object.failure_message
        )

    def get_form(self, form_class=None):
        self.form_object = get_object_or_404(
            Form, slug=self.kwargs.get("slug")
        )
        return self.form_object.as_form(self.request.POST, self.request.FILES)

    def get_success_url(self):
        return self.request.META.get(
            "HTTP_REFERER", self.request.META.get("PATH_INFO")
        )
