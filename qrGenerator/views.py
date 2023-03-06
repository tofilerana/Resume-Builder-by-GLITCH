from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import qrcode
import qrcode.image.svg
from io import BytesIO


def qr(request):
    context = {}
    if request.method == "POST":
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qr_text",""), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()

    return render(request, "webpages/qr.html", context=context)