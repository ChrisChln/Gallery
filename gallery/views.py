from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, Http404
from .models import Image
from .forms import ImageForm
import os
from django.conf import settings
from PIL import Image as PILImage
from PIL import ImageFilter, ImageOps
import json

def image_list(request):
    images = Image.objects.all()
    return render(request, 'gallery/image_list.html', {'images': images})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'gallery/upload_image.html', {'form': form})

def download_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    
    # get the image file path
    file_path = image.image.path
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="image/jpeg")
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
    else:
        # if the image file does not exist, return a 404 error
        from django.http import Http404
        raise Http404("the image does not exist")

from django.shortcuts import render, redirect, get_object_or_404

def edit_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    return render(request, 'gallery/edit_image.html', {'image': image})

def apply_filter(request, filter_type, image_id):  # make sure the filter_type is passed in
    if request.method == 'POST':
        try:
            image = get_object_or_404(Image, id=image_id)
            img_path = image.image.path
            
            # make sure the directory exists
            os.makedirs(os.path.dirname(img_path), exist_ok=True)
            
            # open the image
            img = PILImage.open(img_path)
            
            # filter the image
            if filter_type == 'gray':
                filtered_img = ImageOps.grayscale(img)
                # turn back to RGB mode for saving as JPEG
                filtered_img = filtered_img.convert('RGB')
            elif filter_type == 'blur':
                filtered_img = img.filter(ImageFilter.GaussianBlur(radius=2))
            elif filter_type == 'edge':
                filtered_img = img.filter(ImageFilter.FIND_EDGES)
                # turn back to RGB mode for saving as JPEG
                filtered_img = filtered_img.convert('RGB')
            elif filter_type == 'solar':
                filtered_img = ImageOps.solarize(img, threshold=128)
            else:
                return JsonResponse({'success': False, 'error': '不支持的滤镜类型'})
            
            # sava the image that has been filtered
            filtered_img.save(img_path)
            
            # refresh the image object
            from django.utils import timezone
            cache_buster = int(timezone.now().timestamp())
            
            return JsonResponse({
                'success': True,
                'image_url': f"{image.image.url}?v={cache_buster}"
            })
        except Exception as e:
            import traceback
            print(traceback.format_exc())  # print the error message
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'})

from django.shortcuts import redirect
import os

def delete_image(request, image_id):
    try:
        image = Image.objects.get(id=image_id)
        # delete the image file
        if os.path.exists(image.image.path):
            os.remove(image.image.path)
        # delete the image object
        image.delete()
        return redirect('image_list')
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
