# django-tawea

Add Facebook chat ([Tawea][1]) to a template with a simple tag.


    {% gmapify color='#CC2700' %}

## Installation

Using `pip`:

    $ pip install django-tawea

Or cloning the project from github:

    $ git clone git@javimb/django-tawea.git
    $ cd django-tawea
    $ pip install -r requirements.txt

## Usage

Add `tawea` to `INSTALLED_APPS`:

    INSTALLED_APPS = (
    ...
    'tawea',
    ...)

Load and use the provided `tawea` tag in the template:

    {% load tawea %}
    {% tawea [color=<hex_color>] %}

Django-tawea provides all the JavaScript stuff for Tawea's chat, so put the `tawea` tag at the end of the template.

### Optional args

 - **color:** The hex color used in the chat. #3b5998 by default.

##Example

    {% load tawea %}

    {% block js %}
        {% tawea color='#CC2700' %}
    {% endblock js %}


  [1]: https://tawea.com/