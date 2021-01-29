from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import F, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView
from django.views.generic.base import TemplateView

# from chat.forms import SubscribeConfirm
from chat.models import Message, UserProfile

class SearchView(ListView):
    model = UserProfile
    template_name = 'search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = User.objects.filter(username__icontains=query)
            result = postresult
        else:
            result = None
        return result

class HomeView(LoginRequiredMixin, TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # List all users for chatting. Except myself.
        context['users'] = User.objects.exclude(id=self.request.user.id)\
                                       .values('username')

        return context


class ChatView(LoginRequiredMixin, TemplateView):

    template_name = 'chat.html'

    def dispatch(self, request, **kwargs):
        # Get the person we are chatting with, if not exist raise 404.
        receiver_username = kwargs['chatname'].replace(
            request.user.username, '').replace('-', '')
        kwargs['receiver'] = get_object_or_404(User, username=receiver_username)
        return super().dispatch(request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['receiver'] = kwargs['receiver']
        return context


class MessagesAPIView(View):

    def get(self, request, chatname):
        # Grab two users based on the chat name.
        users = User.objects.filter(username__in=chatname.split('-'))
        # Filters messages between this two users.
        result = Message.objects.filter(
            Q(sender=users[0], receiver=users[1]) | Q(sender=users[1], receiver=users[0])
        ).annotate(
            username=F('sender__username'), message=F('text'),
        ).order_by('date_created').values('username', 'message', 'date_created')

        return JsonResponse(list(result), safe=False)


# class AddToBlacklist(View):
#     def get(self, request, user_name):
#         self_user = User.objects.get(username=user_name)
#         block_init = User.objects.get(username=self_user)
#         self_user_info = UserProfile.objects.get(user=request.user)
#         self_user_info.bl.add(block_init)
#         return redirect('home')
#
#
# class DelFromBL(View):
#     def get(self, request, user_name):
#         self_user = User.objects.get(username=user_name)
#         block_init = User.objects.get(username=self_user)
#         self_user_info = UserProfile.objects.get(user=request.user)
#         self_user_info.bl.remove(block_init)
#         return redirect('home')