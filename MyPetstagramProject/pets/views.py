from django.shortcuts import render, redirect
from MyPetstagramProject.core.photo_utils import apply_likes_count, apply_user_liked_photo
from MyPetstagramProject.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from MyPetstagramProject.pets.models import Pet
from MyPetstagramProject.pets.utils import get_pet_by_name_and_username


def details_pet(request, pet_slug):
    pet = get_pet_by_name_and_username(pet_slug)
    photos = [apply_likes_count(photo) for photo in pet.photo_set.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'pet': pet,
        'photos_count': pet.photo_set.count(),
        'pet_photos': photos,
        # 'is_owner': pet.user == request.user,
    }
    return render(request, 'pets/pet-details-page.html', context,)


def add_pet(request):
    if request.method == 'GET':
        form = PetCreateForm()
    else:
        form = PetCreateForm(request.POST)
        if form.is_valid():
            form.save()
            # pet = form.save(commit=False)
            # pet.user = request.user
            # pet.save()
            return redirect('details user', pk=1)   # TODO: fix this when auth

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-add-page.html', context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()

    # if not is_owner(request, pet):
    #     return redirect('details pet', username=username, pet_slug=pet_slug)

    if request.method == 'GET':
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details pet', username=username, pet_slug=pet_slug)   # TODO: fix this when auth

    context = {
        'form': form,
        'pet_slug': pet_slug,
        'username': username,
    }
    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()

    if request.method == 'GET':
        form = PetDeleteForm(instance=pet)
    else:
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=1)   # TODO: fix this when auth

    context = {
        'form': form,
        'pet_slug': pet_slug,
        'username': username,
    }
    return render(request, 'pets/pet-delete-page.html', context)


