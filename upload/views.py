from django.shortcuts import render,redirect

# Create your views here.
from django.views import View
from .models import PhotoList,DocumentList
from .forms import PhotoListForm,DocumentListForm

import magic

ALLOWED_MIME    = [ "application/pdf" ]

class PhotoView(View):

    def get(self, request, *args, **kwargs):

        data    = PhotoList.objects.all()
        form    = PhotoListForm()

        context = { "data":data,
                    "form":form,
                    }

        return render(request,"upload/index.html",context)

    def post(self, request, *args, **kwargs):

        form    = PhotoListForm(request.POST, request.FILES)
        
        if form.is_valid():
            print("バリデーションOK")
            form.save()

        return redirect("upload:index")

index       = PhotoView.as_view()

class DocumentView(View):

    def get(self, request, *args, **kwargs):

        data    = DocumentList.objects.all()
        form    = DocumentListForm()
        context = { "data":data,
                    "form":form,
                    }

        return render(request,"upload/document.html",context)

    def post(self, request, *args, **kwargs):

        form        = DocumentListForm(request.POST,request.FILES)
        mime_type   = magic.from_buffer(request.FILES["document"].read(1024) , mime=True)

        if form.is_valid():
            print("バリデーションOK")

            if mime_type in ALLOWED_MIME:
                form.save()
            else:
                print("このファイルは許可されていません。")


        return redirect("upload:document")

document    = DocumentView.as_view()
