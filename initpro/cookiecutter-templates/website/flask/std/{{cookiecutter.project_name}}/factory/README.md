How to launch this factory ?
============================
{% if cookiecutter._for_factory %}
The factory {% if not cookiecutter._for_factory[1:] %}only {%endif%}needs{% if cookiecutter._for_factory[1:] %} all{%endif%} the following package{% if cookiecutter._for_factory[1:] %}s{%endif%}. You can use ``pip`` to install {% if cookiecutter._for_factory[1:] %}them{%else%}it{%endif%}.

{%for name, url in cookiecutter._for_factory%}
  1. [{{name}}]({{url}})
{%endfor%}
{% else %}
No extra module is necessary to make the factory works.
{% endif %}
