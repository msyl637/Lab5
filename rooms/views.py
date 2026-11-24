from django.shortcuts import render, redirect
from django.http import Http404
from .models import Room


def archive(request):
    posts = Room.objects.all().order_by('-created_date')
    return render(request, 'archive.html', {"posts": posts})


def get_room(request, room_id):
    try:
        post = Room.objects.get(id=room_id)
        return render(request, 'room.html', {"post": post})
    except Room.DoesNotExist:
        raise Http404


def create_room(request):
    """GET — показать форму. POST — сохранить новый номер."""
    if request.user.is_anonymous:
        raise Http404

    if request.method == "POST":
        form = {
            'title': request.POST.get("title", "").strip(),
            'text': request.POST.get("text", "").strip(),
        }

        if not form["title"] or not form["text"]:
            form['errors'] = "Не все поля заполнены"
            return render(request, 'create_room.html', {'form': form})

        if Room.objects.filter(title=form["title"]).exists():
            form['errors'] = "Номер с таким названием уже существует"
            return render(request, 'create_room.html', {'form': form})

        room = Room.objects.create(
            title=form["title"],
            text=form["text"],
            author=request.user,
        )
        return redirect('get_room', room_id=room.id)

    return render(request, 'create_room.html', {})
