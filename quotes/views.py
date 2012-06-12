# Create your views here.
import json
import random
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from quotes.forms import SubmitQuoteForm
from quotes.models import Quote

def home(request):
    # TODO: use cache machine
    # random_quote = Quote.objects.order_by('?')
    quotes = list(Quote.objects.active())
    if not quotes:
        return HttpResponse('no data available.')

    viewed_quotes = request.session.get('viewed_quotes', [])
    if len(viewed_quotes) == len(quotes):
        viewed_quotes = []

    random_quote = random.choice(filter(
        lambda x : not x.id in viewed_quotes,
        quotes
    ))

    viewed_quotes.append(random_quote.id)
    request.session['viewed_quotes'] = viewed_quotes
    return HttpResponseRedirect(random_quote.get_absolute_url())

def quote(request, id):
    quote = get_object_or_404(Quote.objects.active(), id=id)

    form = SubmitQuoteForm()
    if request.method == "POST":
        form = SubmitQuoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render_to_response('quote.html', context_instance=RequestContext(request, {
        'quote' : quote,
        'submit_quote_form' : form,
        'show_quote_form' : request.method == 'POST'
    }))
