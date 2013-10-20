
EuroDjangoCon 2009
==================

:tags: django, forms, python, talk

EuroDjangoCon 2009 is still going strong, but I wanted to share the materials from my talk as quickly as possible.  My slides are on Slide Share:

.. raw:: html

    <div style="width:425px;text-align:left" id="__ss_1390189"><a style="font:14px Helvetica,Arial,Sans-serif;display:block;margin:12px 0 3px 0;text-decoration:underline;" href="http://www.slideshare.net/kingkilr/forms-getting-your-moneys-worth" title="Forms, Getting Your Money&#39;s Worth">Forms, Getting Your Money&#39;s Worth</a><object style="margin:0px" width="425" height="355"><param name="movie" value="http://static.slidesharecdn.com/swf/ssplayer2.swf?doc=formseurodjangocon-090505150331-phpapp01&stripped_title=forms-getting-your-moneys-worth" /><param name="allowFullScreen" value="true"/><param name="allowScriptAccess" value="always"/><embed src="http://static.slidesharecdn.com/swf/ssplayer2.swf?doc=formseurodjangocon-090505150331-phpapp01&stripped_title=forms-getting-your-moneys-worth" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="425" height="355"></embed></object><div style="font-size:11px;font-family:tahoma,arial;height:26px;padding-top:2px;">View more <a style="text-decoration:underline;" href="http://www.slideshare.net/">documents</a> from <a style="text-decoration:underline;" href="http://www.slideshare.net/kingkilr">Alex Gaynor</a>.</div></div>

And the first examples code follows:


.. sourcecode:: python
    
    from django.forms.util import ErrorList
    from django.utils.datastructures import SortedDict
    
    def multiple_form_factory(form_classes, form_order=None):
       if form_order:
           form_classes = SortedDict([(prefix, form_classes[prefix]) for prefix in
               form_order])
       else:
           form_classes = SortedDict(form_classes)
       return type('MultipleForm', (MultipleFormBase,), {'form_classes': form_classes})
    
    class MultipleFormBase(object):
       def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None,
           initial=None, error_class=ErrorList, label_suffix=':',
           empty_permitted=False):
           if prefix is None:
               prefix = ''
           self.forms = [form_class(data, files, auto_id, prefix + form_prefix,
               initial[i], error_class, label_suffix, empty_permitted) for
               i, (form_prefix, form_class) in enumerate(self.form_classes.iteritems())]
    
       def __unicode__(self):
           return self.as_table()
    
       def __iter__(self):
           for form in self.forms:
               for field in form:
                   yield field
    
       def is_valid(self):
           return all(form.is_valid() for form in self.forms)
    
       def as_table(self):
           return '\n'.join(form.as_table() for form in self.forms)
    
       def as_ul(self):
           return '\n'.join(form.as_ul() for form in self.forms)
    
       def as_p(self):
           return '\n'.join(form.as_p() for form in self.forms)
    
       def is_multipart(self):
           return any(form.is_multipart() for form in self.forms)
    
       def save(self, commit=True):
           return tuple(form.save(commit) for form in self.forms)
       save.alters_data = True

EuroDjangoCon has been a blast thus far and after the conference I'll do a blogpost that does it justice.
