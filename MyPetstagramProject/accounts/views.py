from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model
from MyPetstagramProject.accounts.forms import UserCreateForm

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    # model = UserModel                     # грешно - използвай формата вместо това
    # fields = ('username', 'password')     # грешно - използвай формата вместо това
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')    # като се logout-нем къде искаме да отидем


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    # искаме да добавим допълниелни неща в контекста. Това го правим така:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        # self.request.user е логнатия юзър
        # self.object е селектирания юзър
        # context['pets_count'] = self.object.pet_set.count()
        # context['photos_count'] = self.object.photo_set.count()

        # Photo.objects.select_related()  # взима тези обекти които имат foreign key към текущия обект. Връща QuerrySet
        # Photo.objects.prefetch_related()    # взими свързаните по foreign key неща. Използва се за Many-to-one и many-to-many релации.

        # photos = self.object.photo_set.prefetch_related('photolike_set') # искаме за всичките photos да им вземещ техните photolikes предварително

        # context['likes_count'] = sum(x.photolike_set.count() for x in photos)

        return context


def edit_user(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def delete_user(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
