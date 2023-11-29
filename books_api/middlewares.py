def log_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        print(f'{request.method} {request.path} - {response.status_code}')
        return response

    return middleware
