from django.core.paginator import Paginator
from django.shortcuts import render
from foo.models import Blog

# Create your views here.
def Blogs(request):
    if (request.method ==
            'GET'):
        blogobj = Blog.objects.all()
        # return render(request,'blog.html',{'blogobj':blogobj})

        # book_list = Book.objects.all()
        paginator = Paginator(
            blogobj,
            2
            )
        current_page_num = int(request.GET.get('page', 1))
        if (paginator.num_pages >
                11):
            if (current_page_num - 5 <
                    1):
                page_range = range(
                    1,
                    12
                    )
            elif (current_page_num + 5 >
                  paginator.num_pages):
                page_range = range(
                    paginator.num_pages - 10,
                    paginator.num_pages + 1
                    )
            else:
                page_range = range(
                    current_page_num - 5,
                    current_page_num + 6
                    )
        else:
            page_range = paginator.page_range
        try:
            current_page = paginator.page(current_page_num)
        except EmptyPage as e:
            current_page = paginator.page(1)
        return render(
            request,
            'blog.html',
            locals()
            )