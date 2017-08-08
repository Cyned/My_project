from django.shortcuts import render
from django.views.generic import View


class About(View):
    template_name = 'about/info_page.html'

    def get(self, request):
        return render(request, self.template_name)
