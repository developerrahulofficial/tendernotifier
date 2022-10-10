Python Version >> 3.8.10
Django Version >> 3.2.5


Skote Installation in Django Python

>>>Installation Python
 ->https://www.python.org/downloads/

>>For Windows OS 
 -Download python  from windows store
 -Select the Python's version to download.
 -Click on the Install Now
 -Installation in Process

>>For Linux OS
 -sudo apt update
 -sudo apt install python3
	
>>>Open terminal
 -python --version
 
>>>To check pip version  
  -py -m pip --version
  -upgread pip 
  -py -m pip install --upgrade pip

>>>Installing virtualenv	
  #linux & mac os
   ->python3 -m pip install --user virtualenv
  #Windows
  ->py -m pip install --user virtualenv


>>>Create Virtual Environment
  #linux & mac os
  ->python3 -m venv environment_name
  #Windows
  ->python -m venv environment_name

>>>Activate Environment
  #Linux & mac os
  ->source environment_name/bin/activate
  #Windows
  ->environment_name\Scripts\activate
 
>>>Install Django
 #linux & mac os
 ->pip3 install django
 #Windows
 ->pip install django
 
>>>First please check Django properly Installed or not
 #Linux/macOS
 python3 -m django --version
 #Windows
 python  -m django --version

>>>Open terminal 
 -Goto project directory using cd command
 

>>>Install few libraries
->pip install django-embed-video
->pip install django-crispy-forms

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.#databaseservername#',
        'NAME': '',
        'USER' : '',
        'PASSWORD' : '',
        'HOST' : "localhost",
        'PORT' : '',
                
    }
}
>>>To Create superuser 
->python manage.py createsuperuser
	enter username = your_username
	enter your Email Address
	enter your password
	enter your password again 
-> Windows:-python manage.py migrate
-> Linux:-python3 manage.py migrate

>>>To load Static Files:-
>Go to Skote/setings.py
-Add following command:-
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
STATIC_ROOT= os.path.join(BASE_DIR,'assets')

>Run Command In Terminal
-python manage.py collectstatic


-Goto settings.py of Main Directory

-SMTP CONFIGURATION
	EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
	EMAIL_HOST = 'smtp.gmail.com'
	EMAIL_PORT = 587
	EMAIL_USE_TLS = True
	EMAIL_HOST_USER = 'smtp.gmail.com'
	EMAIL_HOST_PASSWORD = 'Programmer@169'
	DEFAULT_FROM_EMAIL = 'dboy1091997@gmail.com'
	SERVER_EMAIL = 'YOUR EMAIL ADDRESS'
	 



>>>To Set Default Layout
 >Goto templates/partial/base.html
 
<!--===========================================================================-->
                <!--Vertical Layout View-->
<!--===========================================================================-->
#STEP :-1 Select Anyone of following BodyTag 

#Make changes according choice at Line No 23
1.Dark Sidebar
<body data-sidebar="dark">   

2.light sidebar
<body data-sidebar="light"> 

2.Compact Sidebar
<body data-sidebar-size="small">  

3.Icon Sidebar
<body data-keep-enlarged="true" class="vertical-collpsed">  

4.Box Width Sidebar
<body data-keep-enlarged="true" class="vertical-collpsed" data-layout-size="boxed"> 

5.Prealoader Sidebar
 <body data-sidebar=""> 
        <!-- Loader -->
        <div id="preloader">
            <div id="status">
                <div class="spinner-chase">
                    <div class="chase-dot"></div>
                    <div class="chase-dot"></div>
                    <div class="chase-dot"></div>
                    <div class="chase-dot"></div>
                    <div class="chase-dot"></div>
                    <div class="chase-dot"></div>
                </div>
            </div>
        </div> 

6.Colored Sidebar
<body data-sidebar="colored"> 

7.Scrollable Sidebar
<body data-sidebar="dark" data-layout-scrollable="true">

STEP:-2 Select Vertical Header and Siderbar & comment the  Horizontal Header View as shown below.

<!-- VERTICAL LAYOUT VIEW-->
<!--=================================-->

{% block header %}
{% include 'partials/header.html' %}  
{% endblock %}          
{% block sidebar %}
{% include 'partials/sidebar.html' %}   
{% endblock %}    


<!-- HORIZONTAL LAYOUT VIEW-->
<!--=================================-->
{% comment %} {% block header %}
{% include 'partials/hori-header.html' %}
{% endblock %}
{% block sidebar %}
{% include 'partials/hori-sidebar.html' %}
{% endblock %} {% endcomment %}


<!--===========================================================================-->
                        <!--Horizontal Body View-->
<!--===========================================================================-->
#STEP :-1 Select Anyone of following BodyTag 

#Make changes according choice at Line No 23
1.Horizontal Bar
<body data-layout="horizontal" data-topbar="colored"> 

2.Horizontal top dark Bar
<body data-layout="horizontal" data-topbar="dark">  

3.Horizontal Box Width Sidebar
<body data-layout="horizontal" data-topbar="colored" data-layout-size="boxed">  

4.Horizontal Prealoader bar
    <body data-topbar="dark" data-layout="horizontal">

        <!-- Loader -->
        <div id="preloader">
            <div id="status">
                <div class="spinner-chase">
                    <div class="chase-dot"></div>
                    <div class="chase-dot"></div>
                    <div class="chase-dot"></div>
                    <div class="chase-dot"></div>
                    <div class="chase-dot"></div>
                    <div class="chase-dot"></div>
                </div>
            </div>
        </div> 
5.Horizontal colored Header
<body data-topbar="colored" data-layout="horizontal">    

6.Scrollable Horizontal sidebar
<body data-topbar="dark" data-layout="horizontal" data-layout-scrollable="true">

STEP :-2 Comment the Vertical layout view and Siderbar & then Select Horizontal Layout View as shown below.
<!-- VERTICAL LAYOUT VIEW-->
<!--=================================-->
{% comment %}
{% block header %}
{% include 'partials/header.html' %}  
{% endblock %}          
{% block sidebar %}
{% include 'partials/sidebar.html' %}   
{% endblock %} {% endcomment %}   


<!-- HORIZONTAL LAYOUT VIEW-->
<!--=================================-->
{% block header %}
{% include 'partials/hori-header.html' %}
{% endblock %}
{% block sidebar %}
{% include 'partials/hori-sidebar.html' %}
{% endblock %} 

<!--===========================================================================-->

>> To set Default light/dark/RTL Mode
<!--===========================================================================-->
<!--===========================================================================-->

>>Go static/js/app.js
-line number 218
<!--===========================================================================-->


>For Light theme
alreadyVisited = "light-mode-switch";

>For Dark theme
alreadyVisited = "dark-mode-switch";

>For RTL theme
alreadyVisited = "rtl-mode-switch";
# for RTL mode only
-Goto templetes/partials/base.html
 line number 3 
 <html lang="en" dir="rtl">
<!--===========================================================================-->
<!--===========================================================================-->

-> Windows:-python manage.py migrate
-> Linux:-python3 manage.py migrate

>>>Run your project
-Windows:-python manage.py runserver
-Linux:-python3 manage.py runserver
