from django.shortcuts import render
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, content):
    if util.get_entry(content) != None:
        return render(request, "encyclopedia/entry.html", {
            "content": util.get_entry(content),
            "TITLE": content
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "content": f"The {content} page was not found.",
            "TITLE": "Not found"
        })
    
def search(request):
    if request.method == "POST":
        search = request.POST['q']
        if util.get_entry(search) != None:
            return render(request, "encyclopedia/entry.html", {
                "content": util.get_entry(search),
                "TITLE": search
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
    else:
        return render(request, "encyclopedia/search.html", {
            "content": util.list_entries()
        })
    
def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")
    else:
        title = request.POST['title']
        content = request.POST["content"]
        if util.get_entry(title) != None:
            return render(request, "encyclopedia/error.html", {
                "content": f"The {title} page already exists.",
                "TITLE": "Conflicting Error"
            })
        else:
            util.save_entry(title, content)
            return render(request, "encyclopedia/entry.html", {
                "content": content,
                "TITLE": title
            })
        
def edit_page(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit_page.html", {
            "TITLE": title,
            "content": content
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "content": "You are not allowed to do that.",
            "TITLE": "Authorization Error"
        })
    
def save_page(request):
    if request.method == "POST":
        title = request.POST["title"]
        new_content = request.POST["new_content"]
        util.save_entry(title, new_content)
        return render(request, "encyclopedia/entry.html", {
            "content": new_content,
            "TITLE": title
        }) 
    else:
        return render(request, "encyclopedia/error.html", {
            "content": "You are not allowed to do that.",
            "TITLE": "Authorization Error"
        })
    
def random_page(request):
    entries = util.list_entries()
    rand_entry = random.choice(entries)
    return render(request, "encyclopedia/entry.html", {
        "content": util.get_entry(rand_entry),
        "TITLE": rand_entry
    }) 