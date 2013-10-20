
Building a Read Only Field in Django
====================================


One commonly requested feature in Django is to have a field on a form(or in the admin), that is read only.  Such a thing is going may be a Django 1.1 feature for the admin, exclusively, since this is the level that it makes sense at, a form is by definition for inputing data, not displaying data.  However, it is still possible to do this with Django now, and it doesn't even take very much code.  As I've said, doing it in this manner(as a form field) isn't particularly intuitive or sensible, however it is possible.

The first thing we need to examine is how we would want to use this, for our purposes we'll use this just like we would a normal field on a form:

.. sourcecode:: python
    
    from django import forms
    from django.contrib.auth.models import User
    
    class UserForm(forms.ModelForm):
        email = ReadOnlyField()
    
        class Meta:
            model = User
            fields = ['email', 'username']

So we need to write a field, our field will actually need to be a subclass of FileField, at first glance this makes absolutely no sense, our field isn't taking files, it isn't taking any data at all.  However FileFields receive the initial data for their clean() method, which other fields don't, and we need this behavior for our field to work:

.. sourcecode:: python
    
    class ReadOnlyField(forms.FileField):
        widget = ReadOnlyWidget
        def __init__(self, widget=None, label=None, initial=None, help_text=None):
            forms.Field.__init__(self, label=label, initial=initial, 
                help_text=help_text, widget=widget)
    
        def clean(self, value, initial):
            self.widget.initial = initial
            return initial

As you can see in the clean method we are exploiting this feature in order to give our widget the initial value, which it normally won't have access to at render time.

Now we write our ReadOnlyWidget:

.. sourcecode:: python
    
    from django.forms.util import flatatt
    
    class ReadOnlyWidget(forms.Widget):
        def render(self, name, value, attrs):
            final_attrs = self.build_attrs(attrs, name=name)
            if hasattr(self, 'initial'):
                value = self.initial
            return "<p>%s</p>" % (flatatt(final_attrs), value or '')
    
        def _has_changed(self, initial, data):
            return False

Our widget simply renders the initial value to a p tag, instead of as an input tag.  We also override the _has_changed method to always return False, this is used in formsets to avoid resaving data that hasn't changed, since our input can't change data, obviously it won't change.

And that's all there is to it, less than 25 lines of code in all.  As I said earlier this is a fairly poor architecture, and I wouldn't recommend it, however it does work and serves as proof that Django will allow you to do just about anything in you give in a try.
