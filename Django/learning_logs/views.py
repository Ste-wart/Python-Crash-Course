from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Helper functions.
def check_owner(subject, request):
    """Confirms correct user access."""
    if subject.owner != request.user:
        raise Http404('as of now FUCK OFF')


# Create your views here.
def index(request):
    """The home page for Learning Logs."""
    return render(request, 'learning_logs/index.xhtml')


@login_required
def topics(request):
    """Show all topics."""
    subject = Topic.objects.filter(owner=request.user).order_by('date_added')  # querying the database
    context = {'topics': subject}
    return render(request, 'learning_logs/topics.xhtml', context)


@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    subject = Topic.objects.get(id=topic_id)  # querying the database

    # Make sure the topic belongs to the current user
    check_owner(subject, request)

    entries = subject.entry_set.order_by('-date_added')  # querying the database
    context = {'topic': subject, 'entries': entries}

    return render(request, 'learning_logs/topic.xhtml', context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            topic_new = form.save(commit=False)
            topic_new.owner = request.user
            topic_new.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.xhtml', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    subject = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        check_owner(subject, request)
        if form.is_valid():
            new_entries = form.save(commit=False)  # make an instance of the form

            # Set the entry object’s topic attribute before saving it to the database.
            new_entries.topic = subject
            new_entries.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': subject, 'form': form}
    return render(request, 'learning_logs/new_entry.xhtml', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    subject = entry.topic

    # Make sure the entry belongs to the current user.
    check_owner(subject, request)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=entry.topic_id)
    context = {'entry': entry, 'topic': subject, 'form': form}
    return render(request, 'learning_logs/edit_entry.xhtml', context)
