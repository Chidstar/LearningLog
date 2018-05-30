"""Defines URL patterns for users"""

from django.urls import path
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # Login page
    path('login/', login, {'template_name': 'users/login.html'},
            name='login'),
    # Logout page
    path('logout/', views.logout_view, name='logout'),
    # Registration page
    path('register/', views.register, name='register')
    
]

# base.html 
# ~ <p>
  # ~ <a href="{% url 'learning_logs:index' %}">Learning Log</a> -
  # ~ <a href="{% url 'learning_logs:topics' %}">Topics</a> - 
  # ~ {% if user.is_authenticated %}
    # ~ Hello, {{ user.username }}.
	# ~ <a href="{% url 'users:logout' %}">Log out</a>
  # ~ {% else %}
    # ~ <a href="{% url 'users:register' %}">Register</a> - 
    # ~ <a href="{% url 'users:login' %}">Log in</a>
  # ~ {% endif %}
# ~ </p>

# ~ {% block content %}{% endblock content %}

        
