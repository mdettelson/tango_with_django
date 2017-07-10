import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'TangoWithDjango.settings')

import django
django.setup()
from Rango.models import Category, Page

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models

    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/"},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/"},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/"}
    ]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.11/intro/tutorial01/"},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/"},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/"}
    ]

    other_pages = [
        {"title":"Bottle",
         "url":"http://bottlepy.org/docs/dev/"},
        {"title": "Flask",
         "url": "http://flask.pocoo.org"}
    ]

    cats = {"Python": {"pages": python_pages},
            "Django": {"pages": django_pages},
            "Other Frameworks": {"pages": other_pages}
            }
    # Add extra pages to the above dictionaries if you so desire

    # the code below goes through the cats dictionary, then adds each category,
    # and then adds al the associated pages for that category.
    # if you are using ptyon 2.x, use cats.iteritems()

    for cat, cat_data in cats.iteritems():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    # Print out categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print ("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    # get_or_create returns a tuple, therefore we need to specify we
    # want the object and not the boolean
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

# allows this to be used as package or as an independent app
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()