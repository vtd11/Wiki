from django.http import HttpResponse
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, content):
    if util.get_entry(content) != None:
        return render(request, "encyclopedia/entry.html", {
            "content": util.get_entry(content),
            "TITLE": content.capitalize()
        })
    else:
        error= f"The {content} page was not found."
        return render(request, "encyclopedia/entry.html", {
            "content": error,
            "TITLE": content.capitalize()
        })
    
def search(request):
    search = request.POST['q']
    if util.get_entry(search) != None:
        return render(request, "encyclopedia/entry.html", {
            "content": util.get_entry(search),
            "TITLE": search.capitalize()
        })
    else:
        entries = util.list_entries()
        results = []
        for entry in entries:
            if search.lower() in entry.lower():
                results.append(entry)
        return render(request, "encyclopedia/search.html", {
            "content": results
        })