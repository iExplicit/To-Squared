from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from squared_app.models import Squared
# Create your views here.

def index(request):
    items = []
    filter = None
    count_pending_items = 0
    count_done_items = 0
    # Get only the user-specific todo items.
    if request.user.is_authenticated:
        filter = request.GET.get('filter')
        print('Filter = ', filter)
        

        items = filter_results(request.user, filter)
        
        for item in items:
            if item.done == False:
                count_pending_items += 1
            else:
                count_done_items += 1

    return render(request, 'index.html', {
        'items': items,
        'filter': filter,
        'count_pending_items' : count_pending_items,
        'count_done_items' : count_done_items
    })


def filter_results(user, filter):
    # If filter is completed
    if filter == 'done':
        return Squared.objects.filter(
            user=user,
            done=True
        ).order_by('created_at')
        

    # Else If filter is pending
    elif filter == 'pending':
        return Squared.objects.filter(
            user=user,
            done=False
        ).order_by('created_at')
        

    # Otherwise
    else:
        return Squared.objects.filter(user=user).order_by('created_at')

@login_required
def create(request):
    return render(request, 'form.html', {
        'form_type': 'create'
    })
@login_required
def save(request):
    # Get the form data from the request.
    title = request.POST.get('title')
    description = request.POST.get('description')

    # Get hidden form data.
    form_type = request.POST.get('form_type')
    id = request.POST.get('id')

    print('Form type received:', form_type)
    print('Form squared id received:', id)

    # Validation logic
    if title is None or title.strip() == '':
        messages.error(request, 'Item not saved. Please provide the title.')
        return redirect(request.META.get('HTTP_REFERER'))

    if form_type == 'create':
        # Create a new todo item with the data.
        squared = Squared.objects.create(
            title=title,
            description=description,
            created_at=timezone.now(),
            user=request.user
        )
        print('New Squared created: ', squared.__dict__)
    elif form_type == 'edit' and id.isdigit():
        squared = Squared.objects.get(pk=id)
        print('Got squared item: ', squared.__dict__)

        # Save logic
        squared.title = title
        squared.description = description

        squared.save()
        print('squared updated: ', squared.__dict__)

    # Add save success message
    messages.info(request, 'Squared Item Saved.')
    # Redirect back to index page
    return redirect('index')


@login_required
def edit(request, id):
    print('Received Id: ' + str(id))

    # Fetch todo item by id
    squared = Squared.objects.get(pk=id)
    print('Got squared item: ', squared.__dict__)

    # Check if the logged in user is the creator user of todo.
    if request.user.id != squared.user.id:
        messages.error(
            request, 'You are not authorized to edit this squared item.')
        return redirect('index')

    return render(request, 'form.html', {
        'form_type': 'edit',
        'todo': squared
    })


@login_required
def delete(request, id):
    # Fetch todo item by id
    squared = Squared.objects.get(pk=id)
    print('Got todo item: ', squared.__dict__)

    # Check if the logged in user is the creator user of todo.
    if request.user.id == squared.user.id:
        messages.info(request, 'Todo Item has been deleted.')
        squared.delete()
        return redirect('index')

    messages.error(request, 'You are not authorized to delete this todo item.')
    return redirect('index')
