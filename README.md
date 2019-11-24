# Flask_App
Simple Flask_Restful App from Udemy course


## Procfile
A Procfile specifies the commands that are executed by the app on startup, e.g. the used web server, worker processes, scheduled jobs etc.
A Procfile declares its process types on individual lines, each with the format  <process type>: <command>


<process type> is an alphanumeric name for a command, such as web, worker, urgentworker, clock, and so on.
<command> indicates the command that every dyno of the process type should execute on startup, such as rake jobs:work.

The process web is the only process that is allowed to receive external http traffic. If the app uses a web server this should be declared as the app's web process, e.g. web: uwsgi uwsgi.ini


## Dyno
Dynos are isolated, virtualized Unix containers, that provide the environment required to run an application.


## WSGI
WSGI[1] is not a server, a python module, a framework, an API or any kind of software. It is just an interface specification by which server and application communicate. Both server and application interface sides are specified in the PEP 3333. If an application (or framework or toolkit) is written to the WSGI spec then it will run on any server written to that spec.
http://wsgi.tutorial.codepoint.net
