from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .forms import ResultForm
from .scripts.test import test_func
from django.conf import settings
import PIL
import os
import shutil


def index(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)  # Do not forget to add: request.FILES
        if form.is_valid():
            image_path = form.save().image.path
            #evaluate = test_func(image_path)
            resultform = ResultForm(initial={"answer": "thumb_up"})
            #os.remove(image_path)
            return HttpResponse("<h2>Результат проверки: {0}</h2>".format(image_path))
            #return render(request, "result.html", {"my_text_1": "{0}: {1}%".format('thumb_up', round((evaluate['thumb_up']*100),3)),
            #                                       "my_text_2": "{0}: {1}%".format('ok', round((evaluate['ok']*100),3)),
            #                                       "my_path": "/media/"+os.path.basename(image_path),
            #                                       "image_name": os.path.basename(image_path),
            #                                       "form": resultform})
        return HttpResponse("<h2>Произошла ошибка {0}</h2>".format(""))
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})


def result(request):
    if request.method == "POST":
        image_name = request.POST['image_name']
        old_name = settings.MEDIA_ROOT + "\\" + image_name
        new_name = settings.MEDIA_ROOT + "\\" + request.POST['answer'] + "\\" + image_name
        shutil.copyfile(old_name, new_name)
        str = "Файл сохранен в: /media/" + request.POST['answer'] + "/" + image_name + " c вероятностью 100%." \
                                                                                        " Спасибо за обучение сети!"
        return render(request, "text.html", {"my_text": str})
