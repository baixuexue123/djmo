# -*- coding: utf-8 -*-


class CustomMiddleware(object):

    def process_request(self, request):
        """
        :param request: HttpRequest object.
        :return: return either None or an HttpResponse object.
            If it returns None, Django will continue processing this request,
        executing any other process_request() middleware, then, process_view() middleware,
        and finally, the appropriate view.
            If it returns an HttpResponse object, Django won’t bother calling any other request,
        view or exception middleware, or the appropriate view;
        it’ll apply response middleware to that HttpResponse, and return the result.
        """
        pass

    def process_view(self, request, callback, callback_args, callback_kwargs):
        """
        this func is called just before Django calls the view.
        :param request: HttpRequest object.
        :param callback: It’s the actual function object, not the name of the function as a string
        :param callback_args:
        :param callback_kwargs:
        :return:  return either None or an HttpResponse object.
        """
        pass

    def process_template_response(self, request, response):
        """
        :param request: HttpRequest object.
        :param response: TemplateResponse returned by a Django view or by a middleware.
        :return : must return a response object that implements a render method
        """
        pass

    def process_response(self, request, response):
        """
        :param request: HttpRequest object.
        :param response: HttpResponse or StreamingHttpResponse returned by a Django view or by a middleware.
        :return : must return an HttpResponse or StreamingHttpResponse object.
        """
        pass

    def process_exception(self, request, exception):
        """
        :param request: HttpRequest object.
        :param exception: is an Exception object raised by the view function.
        :return: None or an HttpResponse object
            If it returns an HttpResponse object, the template response and response middleware will be applied,
        and the resulting response returned to the browser. Otherwise, default exception handling kicks in.
        """
        pass
