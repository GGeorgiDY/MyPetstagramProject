import pyperclip
from django.shortcuts import render, redirect
from django.urls import reverse
from MyPetstagramProject.common.models import PhotoLike
from MyPetstagramProject.common.utils import get_photo_url
from MyPetstagramProject.core.photo_utils import apply_likes_count, apply_user_liked_photo
from MyPetstagramProject.photos.models import Photo


def index(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]
    context = {
        'photos': photos,
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