from django import template

register = template.Library() #assigning the library to register

@register.filter(name='cut')
def cut(value,arg): #custom filter the value to affect and args
    """
    This cuts all values of "arg"from string!
    
    """
    return value.replace(arg,'') #pythong string operation look for the arg value and replace with the secnd arguments

# register.filter('cut',cut)