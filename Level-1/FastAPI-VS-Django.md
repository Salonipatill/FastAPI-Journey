| FastAPI                                          | Django                           |
| ------------------------------------------------ | -------------------------------- |
| Lightweight                                      | Full-featured framework          |
| Mainly used for APIs/backend services            | Full web applications            |
| Automatic API documentation                      | Not its primary built-in feature |
| Very flexible architecture                       | More batteries-included          |
| ASGI support                                     | Supports ASGI and WSGI           |
| Usually choose your own database/auth/etc. tools | Many features included           |



WSGI (Web Server Gateway Interface) is a standard interface that allows a web server to communicate with a Python web application.


WSGI = a standard way for web servers and Python web applications to communicate.

Flask commonly uses WSGI.

Flask was originally designed around WSGI, which is mainly synchronous, while ASGI was later designed to support asynchronous applications.


Flask → WSGI → synchronous web applications
FastAPI → ASGI → asynchronous + synchronous applications