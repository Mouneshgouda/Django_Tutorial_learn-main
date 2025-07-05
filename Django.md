## Basic 

```python
pip install virtualenv  
python -m venv env
.\env\Scripts\activate


pip install django


# Create the Django project (same as django-admin startproject)
python -m django startproject mysite

# Move into the project directory
cd mysite

# Create the Django app (same as django-admin startapp)
python -m django startapp blog


```


## Creation
```
django-admin startproject mysite
cd mysite
python manage.py startapp blog
```

## setup
```python
INSTALLED_APPS = [
    ...
    'pages',
]
```

### blog.urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),  # ✅ New URL
]
```



## blog/views.py
```


from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def feedback(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Feedback from {name} ({email}): {message}')
        success = True
    return render(request, 'pages/feedback.html', {'success': success})


```


## blog/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
]


```

## mysite/urls.py
```python
"""

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('blog.urls')),
]


```


```python
pages/
│
├── templates/
│   └── pages/
│       ├── home.html
│       ├── about.html
│       └── contact.html

```

# home.html
```python

<!DOCTYPE html>
<html>
<head><title>Home</title></head>
<body>
    <h1>Hello from Home Page</h1>
    <a href="/about/">About</a> | <a href="/contact/">Contact</a> | <a href="/feedback/">Feedback</a>

</body>
</html>



```

## about.html
```python
<!DOCTYPE html>
<html>
<head><title>About</title></head>
<body>
    <h1>This is About Page</h1>
    <a href="/">Home</a> | <a href="/contact/">Contact</a>
</body>
</html>

```

## contact.html
```
<!DOCTYPE html>
<html>
<head><title>Contact</title></head>
<body>
    <h1>This is Contact Page</h1>
    <a href="/">Home</a> | <a href="/about/">About</a>
</body>
</html>

```


## 📁 Step 1: Update pages/urls.py
```python

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),  # ✅ New URL
]

```


```python
<!DOCTYPE html>
<html>
<head>
    <title>Feedback</title>
</head>
<body>
    <h1>Feedback Page</h1>
    
    {% if success %}
        <p style="color: green;">Thank you for your feedback!</p>
    {% endif %}

    <form method="post">
        {% csrf_token %}
        <label>Name:</label><br>
        <input type="text" name="name" required><br><br>

        <label>Email:</label><br>
        <input type="email" name="email" required><br><br>

        <label>Message:</label><br>
        <textarea name="message" rows="4" required></textarea><br><br>

        <button type="submit">Submit</button>
    </form>

    <br>
    <a href="/">Back to Home</a>
</body>
</html>
```
