from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from web_app.models import UserProfile
from .forms import EditProfileForm, ProfilePageForm, SignUpForm, EditSettingsForm, PasswordChangingForm

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserSettingsView(generic.UpdateView):
    form_class = EditSettingsForm
    template_name = 'registration/edit_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class ShowProfilePageView(DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        indv_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        context["indv_user"] = indv_user
        return context

class EditProfilePageView(generic.UpdateView):
    model = UserProfile
    form_class = EditProfileForm
    template_name = 'registration/edit_user_profile.html'
    #fields = ['bio', 'profile_pic', 'git_url', 'lnkdin_url']

class CreateProfilePageView(generic.CreateView):
    model = UserProfile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)