How to launch all the tests ?
=============================
{% if cookiecutter._for_test %}
The tests {% if not cookiecutter._for_test[1:] %}only {%endif%}need{% if cookiecutter._for_test[1:] %} all{%endif%} the following package{% if cookiecutter._for_test[1:] %}s{%endif%}. You can use ``pip`` to install {% if cookiecutter._for_test[1:] %}them{%else%}it{%endif%}.

{%for name, url in cookiecutter._for_test%}
  1. [{{name}}]({{url}})
{%endfor%}
{% else %}
No extra module is necessary to make the tests work.
{% endif %}
