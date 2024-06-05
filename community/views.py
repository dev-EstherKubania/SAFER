from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from alerts.models import WeatherAlert
from .models import Region, Forum, Message, Media
from .forms import MessageForm, CreateForumForm

# Create your views here.
@login_required
def community_home(request):
    form = CreateForumForm()
    regions = Region.objects.all()
    forums = Forum.objects.all()
    alerts = WeatherAlert.objects.all()

    context = {
        'regions': regions,
        'forums': forums,
        'form': form,
        'alerts': alerts,
    }

    return render(request, 'community/index.html', context)


@login_required
def create_forum(request):
    form = CreateForumForm
    regions = Region.objects.all()

    if request.method == 'POST':
        region_name = request.POST.get('region')
        region, created_at = Region.objects.get_or_create(name=region_name)

        new_forum = Forum.objects.create(
            owner=request.user,
            region=region,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        new_forum.members.add(request.user)
        return redirect('community-home')

    context = {
        'form': form,
        'regions': regions
    }
    return redirect('community-home', context)


@login_required
def forum(request, forum_id):
    regions = Region.objects.all()
    forum = Forum.objects.get(id=forum_id)
    messages = Message.objects.filter(forum=forum).select_related('media', 'sender')
    # form = MessageForm()

    context = {
        'regions': regions,
        'forum': forum,
        'messages': messages,
        # 'form': form
    }

    return render(request, 'community/forum.html', context)

def upload_media(request):
    if request.method == 'POST':
        media = Media(file=request.FILES['file'])
        media.save()
        # print('Media saved from upload_media view')
        return JsonResponse({'media_url': media.file.url})
    return JsonResponse({'error': 'Invalid request'}, status=400)

