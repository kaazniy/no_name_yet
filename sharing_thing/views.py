from django.shortcuts import render

lessons = [
    {
        'author':'Kazankov Arseniy',
        'title':'Games',
        'content':'First lesson content',
        'date_posted':'December 12, 2023'
    },
    {
        'author':'Soldatove Sofya',
        'title':'Combinatorics',
        'content':'Second lesson content',
        'date_posted':'December 13, 2023'
    }
]


def home(request):
    context =  {
        'lessons':lessons
    }
    return render(request, 'sharing_thing/home.html',context)

def about(request):
    return render(request,'sharing_thing/about.html')
