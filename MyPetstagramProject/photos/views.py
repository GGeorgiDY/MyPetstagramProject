from django.shortcuts import render, redirect
from MyPetstagramProject.common.utils import get_user_liked_photos
from MyPetstagramProject.photos.forms import PhotoDeleteForm, PhotoCreateForm, PhotoEditForm
from MyPetstagramProject.photos.models import Photo


# @login_required
def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)   # без request.FILES няма да се качи снимката
        if form.is_valid():
            # photo = form.save(commit=False)
            # photo.user = request.user
            # photo.save()
            # form.save_m2m()             # викаме го за да хване pk
            photo = form.save()           # form.save() returns the object saved
            return redirect('details photo', pk=photo.pk)

    context = {
        'form': form,
    }
    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    # user_liked_photos = Photo.objects.filter(pk=pk, user_id=request.user.pk,)

    context = {
        'photo': photo,
        'has_user_liked_photo': get_user_liked_photos(pk),
        'likes_count': photo.photolike_set.count(),
        # 'is_owner': request.user == photo.user,
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = PhotoEditForm(instance=photo)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('details photo', pk=photo.pk)  # TODO: fix this when auth

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = PhotoDeleteForm(instance=photo)
    else:
        form = PhotoDeleteForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, 'photos/photo-delete-page.html', context)

