# django-la-links
Django app for a simple links management 

- Copy `links` APP folder to your project;

- Add links into `INSTALLED_APPS`;

- Execute `python manage.py syncdb`;

- Call the templatetags into your template: `{% load links_list %}`

- List the links provided by templatetags. Ex.:
    ``` html
    {% get_links as links %}
    {% for link in links %}
    <a href="{{link.url}}" title="{{link.description}}">{{link.title}}</a>
    {% endfor %}
    ```