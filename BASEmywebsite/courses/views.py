from django.shortcuts import render,get_object_or_404
from .models import Course,Category,Tags

# Create your views here.

# def courses(request):
#     courses=Course.objects.all()
#     categories=Category.objects.all()
#     tags=Tags.objects.all()
#     context = {
#         'courses':courses,
#         'categories':categories,
#         'tags':tags

#     }


#     return render(request, 'courses.html',context)



def course_list(request,category_slug=None,tags_slug=None):
    category_page=None
    tag_page=None
    categories=Category.objects.all()
    tags=Tags.objects.all()
    current_user =request.user

    if category_slug != None:
        category_page = get_object_or_404(Category,slug=category_slug)
        courses = Course.objects.filter(available=True, category=category_page)
    elif category_slug != None:
         tags_page = get_object_or_404(Tags,slug=tags_slug)
         courses = Course.objects.filter(available=True, tags=tags_page)
    else:
        if current_user.is_authenticated:
            enrolled_courses=current_user.courses_joined.all()
            courses=Course.objects.all().order_by('-created_date')          
            for course in enrolled_courses:
                courses=courses.exclude(id=course.id)
        else:
            courses=Course.objects.all().order_by('-created_date')


    
    context={
        'courses':courses,
        'categories':categories,
        'tags':tags
    }
    return render(request,'courses.html',context)



def course_detail(request,category_slug,course_id):
    current_user =request.user
    course = Course.objects.get(category__slug = category_slug, id = course_id )
    courses=Course.objects.all().order_by('-created_date')
    categories=Category.objects.all()
    tags=Tags.objects.all()
    
    if current_user.is_authenticated:
        
        enrolled_courses=current_user.courses_joined.all()
    else:
        enrolled_courses=courses

    


    context = {
        'course': course,
        'enrolled_courses': enrolled_courses,
        'categories':categories,
        'tags':tags
    } 

    return render(request, 'course.html', context)


   


# def category_list(request,category_slug):
#     courses=Course.objects.all().filter(category__slug=category_slug)
#     categories=Category.objects.all()
#     tags=Tags.objects.all()
    
#     context={
#         'courses':courses,
#         'categories':categories,
#         'tags':tags
#     }
#     return render(request,'courses.html',context)


    

# def tags_list(request,tags_slug):
#     courses=Course.objects.all().filter(tags__slug=tags_slug)
#     categories=Category.objects.all()
#     tags=Tags.objects.all()
    
#     context={
#         'courses':courses,
#         'categories':categories,
#         'tags':tags
#     }
#     return render(request, 'courses.html',context)

