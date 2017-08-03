from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from .models import Post
from .forms import UserForm, PostForm, UserFormLog
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Home(View):
    template_name = 'home/home_page.html'

    def get(self, request):
        context = {
            'posts': Post.objects.all(),
        }
        if authenticate() is not None:
            context.update({'online': True})

        return render(request, self.template_name, context)


class DetailUser(DetailView):
    model = User
    template_name = 'home/detail_user.html'


class Create_post(View):
    form_class = PostForm
    template_name = 'home/post_form.html'

    @method_decorator(login_required)
    def get(self, request, pk=0):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk=0):
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.date = timezone.now()
            post.save()
            return redirect('home:home')
        return render(request, self.template_name, {'form': self.form_class(None)})


class Log_in(View):
    form_class = UserFormLog
    template_name = 'home/log_page.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = form['username'].value()
        password = form['password'].value()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')
        return redirect('home:login')


class Log_out(View):
    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return redirect('home:home')


class Log_up(View):
    form_class = UserForm
    template_name = 'home/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            login(request, user)
            return redirect('home:home')
        return redirect('home:log_up')
