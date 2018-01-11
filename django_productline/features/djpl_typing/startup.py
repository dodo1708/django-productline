import monkeytype


def refine_get_wsgi_application(original):
    def get_wsgi_application():
        from django_productline import startup
        startup.select_product()
        from django.core.wsgi import get_wsgi_application
        app = get_wsgi_application()

        def wrapper(environ, start_response):
            with monkeytype.trace():
                return app(environ, start_response)

        return wrapper
    return get_wsgi_application
