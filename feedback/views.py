from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

import user
from feedback.feedback_form import FeedbackForm
from feedback.models import Feedbacks


def dashboard(request):
    context = {
        'posts': Feedbacks.objects.all()
    }
    return render(request, 'list_view.html', context)


class IndexView(LoginRequiredMixin, ListView):
    model = Feedbacks
    template_name = 'list_view.html'
    context_object_name = 'index_post_list'
    permission_denied_message = "You are not allowed here."


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Feedbacks
    form_class = FeedbackForm
    template_name = 'add_view.html'
    success_url = reverse_lazy('manage_post_list')
    permission_denied_message = "You are not allowed here."

    def user_info(self):
        current_user = self.user.username
        return current_user


class ManagePostList(LoginRequiredMixin, ListView):
    model = Feedbacks

    template_name = 'manage_post_list.html'
    context_object_name = 'manage_post_list'
    permission_denied_message = "You are not allowed here."


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Feedbacks
    form_class = FeedbackForm
    pk_url_kwarg = 'pk'
    template_name = 'edit_view.html'
    success_url = '/feedback/manage_post_list/'
    permission_denied_message = "You are not allowed here."

    def form_valid(self, form):
        form.instance.username = self.request.user.username
        return super().form_valid(form)

    def test_func(self):
        feedback = self.get_object()
        if self.request.user == feedback.user:
            return True
        return False


class DetailedView(DetailView):
    model = Feedbacks
    pk_url_kwarg = 'pk'
    template_name = 'detail_view.html'
    context_object_name = 'post'


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Feedbacks
    pk_url_kwarg = 'pk'
    template_name = 'delete_view.html'
    success_url = '/feedback/manage_post_list/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
