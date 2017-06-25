from django.shortcuts import render_to_response
from .models import Book, Page
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

def home(request):
    return render_to_response('home.html')


def searching(search_text):
    final_result = []
    search_in_title = Book.objects.filter(title__icontains=str(search_text))
    for i in search_in_title:

        book_dict = {'word': search_text, 'where': 'title', 'book': i.title}
        final_result.append(book_dict)

    search_in_table = Book.objects.filter(table_of_content__icontains=str(search_text))
    for i in search_in_table:

        book_dict = {'word': search_text, 'where': 'table', 'book': i.title}
        final_result.append(book_dict)

    search_in_page = Page.objects.filter(content__icontains=str(search_text))
    for i in search_in_page:

        book_dict = {
            'word': search_text,
            'where': 'page',
            'page': i.number,
            'chapter': i.chapter,
            'book_id': i.book_id.title
        }
        final_result.append(book_dict)

    return final_result


def make_letter(searching_result):
    mailing_text = 'The result of searching is ...'
    for i in searching_result:
        if i['where'] == 'title':
            mailing_text += '\n The word: {word} has found in Title of the book: {book}'\
                .format(word=i['word'], book=i['book'])
        elif i['where'] == 'table':
            mailing_text += '\n The word: {word} has found in Table of content of the book: {book}'\
                .format(word=i['word'], book=i['book'])
        elif i['where'] == 'page':
            mailing_text += '\n The word:{word} has found in {chapter} chapter, on {page} page of the book: {book}'\
                .format(word=i['word'], chapter=i['chapter'], page=i['page'], book=i['book_id'])
        else:
            mailing_text += '\n TEXT NOT FOUND'
    return mailing_text


def mailing(letter, user_email):
    send_mail(
        'The result of your request',
        letter,
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False
    )


@csrf_exempt
def input_text(request):
    user_email = 'user email was not entered'
    if request.method == 'POST':
        user_email = request.POST.get('user_email')
        my_word = request.POST.get('word')
        searching_result = searching(my_word)     # list of dict
        letter = make_letter(searching_result)
        mailing(letter, user_email)

    return render(request, 'search_send.html', {'user_email': user_email})
