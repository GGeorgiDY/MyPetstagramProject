import pyperclip
from django.shortcuts import render, redirect
from django.urls import reverse
from MyPetstagramProject.common.forms import PhotoCommentForm
from MyPetstagramProject.common.models import PhotoLike
from MyPetstagramProject.common.utils import get_photo_url
from MyPetstagramProject.core.photo_utils import apply_likes_count, apply_user_liked_photo
from MyPetstagramProject.photos.models import Photo


def index(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]
    context = {
        'photos': photos,
        'comment_form': PhotoCommentForm(),
    }

    return render(request, 'common/home-page.html', context)


def like_photo(request, photo_id):
    user_liked_photos = PhotoLike.objects.filter(photo_id=photo_id)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
        # create създава обект с **kwargs и го извиква
        PhotoLike.objects.create(
            photo_id=photo_id,
        )

    return redirect(get_photo_url(request, photo_id))


def share_photo(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={'pk': photo_id})
    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))


def comment_photo(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()
    # тук не е необходимо да си правим if == GET понеже тук имаме само POST метод
    form = PhotoCommentForm(request.POST)

    # ако е валидна формата, тогава запази коментара
    if form.is_valid():
        # правейки го по този начин
        comment = form.save(commit=False)   # does not persist to DB
        comment.photo = photo
        comment.save()

    return redirect('index')