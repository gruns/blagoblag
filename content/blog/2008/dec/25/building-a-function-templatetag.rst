
Building a Function Templatetag
===============================

:tags: django, template

One of the complaints often lobbied against Django's templating system is that there is no way to create functions.  This is intentional, Django's template language is not meant to be a full programming language.  However, if one wants to it is entirely possible to build a templatetag to allow a user to create, and call functions in the template language.


To get started we need to build a tag to create functions, first we need our parsing function:

.. sourcecode:: python
    
    from django import template
    
    register = template.Library()
    
    @register.tag
    def function(parser, token):
        arglist = token.split_contents()[1:]
        func_name = arglist.pop(0)
        nodelist = parser.parse(('endfunction',))
        parser.delete_first_token()
        return FunctionNode(func_name, arglist, nodelist)

The format for our tag is going to be {% function func_name arglist... %}.  So we parse this out of the token.  We get everything after the initial piece of the function definition, we make the first part of this the function name, and the rest is the argument list.  The next part is to parse until the {% endfunction %} tag.  Finally we return a FunctionNode.  Now we need to actually build this node:


.. sourcecode:: python
    
    class FunctionNode(template.Node):
        def __init__(self, func_name, arglist, nodelist):
            self.func_name = func_name
            self.nodelist = nodelist
            self.arglist = arglist
    
        def render(self, context):
            if '_functions' not in context:
                context['_functions'] = {}
            context['_functions'][self.func_name] = (self.arglist, self.nodelist)
            return ''

Our __init__ method just stores the data on the instance.  Our render method stores the argument list and the nodes that make up the function in the context.  This gives us all the information we will need to know in order to call and render our functions.  Now we need our actual mechanism for calling our functions:


.. sourcecode:: python
    
    @register.tag
    def call(parser, token):
        arglist = token.split_contents()[1:]
        func_name = arglist.pop(0)
        return CallNode(func_name, arglist)

Like our function tag, we parse out the name of the function, and then the argument list.  And now we need to render the result of calling it:

.. sourcecode:: python
    
    class CallNode(template.Node):
        def __init__(self, func_name, arglist):
            self.func_name = func_name
            self.arglist = arglist
    
        def render(self, context):
            arglist, nodelist = context['_functions'][self.func_name]
            c = template.Context(dict(zip(arglist, [template.Variable(x).resolve(context) for x in self.arglist])))
            return nodelist.render(c)

render gets the arglist and nodelist out of the context, and then creates a context of the calling variables, by zipping together the variable names from function definition and function calling.

Now we can create functions by doing:

.. sourcecode:: html+django
    
    {% function f arg %}
        {{ arg }}
    {% endfunction %}

And call them by doing:

.. sourcecode:: html+django
    
    {% call f some_var %}
    {% call f some_other_var %}

Hopefully this has given you a useful insight into how to build powerful templatetags in Django's template language.  One possible improvement the reader may want to do is to have the function tag actually register a templatetag out of the function definition, and then be able to use it by simpling using it like a normal templatetag.  As a slight warning I haven't tested this with a wide range of data, so if there are any issues please report them.
