from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry, Article, Comment
from .forms import TopicForm, EntryForm, CommentForm


def index(request):
    """The home page for Learning Log."""
    return render(request, 'new_sites/index.html')


def about(request):
    """Basic information about this site."""
    return render(request, 'new_sites/about.html')


@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'new_sites/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'new_sites/topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('new_sites:topics'))

    context = {'form': form}
    return render(request, 'new_sites/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
        return HttpResponseRedirect(reverse('new_sites:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'new_sites/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('new_sites:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'new_sites/edit_entry.html', context)


@login_required
def delete_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    entry.delete()
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    else:
        return HttpResponseRedirect(reverse('new_sites:topic', args=[topic.id]))


def success(request):
    """Basic information about this site."""
    return render(request, 'new_sites/success.html')


def articles(request):
    """Basic information about this site."""
    articles = Article.objects.order_by('date_added')
    context = {'articles': articles}
    return render(request, 'new_sites/articles.html', context)


def article(request, article_id):
    """Show a single article and all its entries."""
    article = Article.objects.get(id=article_id)
    articlesentries = article.articleentry_set.order_by('-date_added')
    context = {'article': article, 'articlesentries': articlesentries}
    return render(request, 'new_sites/article.html', context)


def add_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return HttpResponseRedirect(reverse('new_sites:article', args=[article.id]))
    else:
        form = CommentForm()
    return render(request, 'new_sites/add_comment.html', {'form': form})
