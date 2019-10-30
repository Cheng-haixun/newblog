from django.shortcuts import render, redirect
from foo.models import Blog,Comment,User

# Create your views here.
def Post(request,b_id):
    if (request.method ==
            'GET'):
        blog = Blog.objects.filter(b_id=b_id).first()
        blogobj = Blog.objects.all()
        comments = Comment.objects.filter(blogobj=b_id).all()
        # userobj = User.objects.filter(userobj=1)
        return render(
            request,
            'post.html',
            locals()
            )
    if (request.method ==
            'POST'):
        username = request.POST.get("username")
        email = request.POST.get("email")
        comment = request.POST.get("comment")
        # print(username,email,comment)
        blogobj = Blog.objects.filter(b_id=b_id).first()
        blogobj.commentcount += 1
        blogobj.save()
        user = User.objects.filter(
                u_name=username,
                u_email=email
                ).first()
        # print(user.u_id)
        if user:
            Comment.objects.create(
                content=comment,
                userobj=user,
                blogobj=blogobj
                )
        else:
            User.objects.create(
                u_name=username,
                u_email=email
                )
            user = User.objects.filter(
                u_name=username,
                u_email=email
                ).first()
            Comment.objects.create(
                content=comment,
                userobj=user,
                blogobj=blogobj
                )
        return redirect('/post/%s'%(b_id))