# Importe os módulos necessários do Django
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import Book

books = []

# Defina a classe de visualização para manipular as operações CRUD de livros
@method_decorator(csrf_exempt, name='dispatch')  # Desativa a proteção CSRF para simplificar o exemplo
class BookView(View):
    # Rota para listar todos os livros
    @method_decorator(require_GET)
    def get(self, request):
        print('Endpoint de listagem de livros acessado')
        return JsonResponse(books, safe=False)

    # Rota para criar um novo livro
    @method_decorator(require_POST)
    def post(self, request):
        data = json.loads(request.body)
        title = data.get('title')
        author = data.get('author')
        id = len(books) + 1  # Simplesmente use o próximo número inteiro como ID (não recomendado para produção)
        new_book = {'id': id, 'title': title, 'author': author}
        books.append(new_book)
        print(f'Novo livro criado: {new_book["title"]} por {new_book["author"]}')
        return JsonResponse(new_book, status=201)

    # Rota para atualizar um livro por ID
    @method_decorator(require_http_methods(["PUT"]))
    def put(self, request, id):
        book = get_object_or_404(books, id=id)
        data = json.loads(request.body)
        book['title'] = data.get('title', book['title'])
        book['author'] = data.get('author', book['author'])
        print(f'Livro atualizado: {book["title"]} por {book["author"]}')
        return JsonResponse(book)

    # Rota para excluir um livro por ID
    @method_decorator(require_http_methods(["DELETE"]))
    def delete(self, request, id):
        book = get_object_or_404(books, id=id)
        books.remove(book)
        print(f'Livro excluído: {book["title"]} por {book["author"]}')
        return JsonResponse({'message': 'Livro excluído com sucesso'})

