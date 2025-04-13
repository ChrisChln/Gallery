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
    
    try:
        file_name = os.path.basename(image.image.name)
        file_content = image.image.read()
        

        http_response = HttpResponse(file_content, content_type="image/jpeg")
        http_response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return http_response
    except Exception as e:
        from django.http import Http404
        print(f"download fail: {str(e)}")
        raise Http404(f"Image does not exist: {str(e)}")

from django.shortcuts import render, redirect, get_object_or_404

def edit_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    return render(request, 'gallery/edit_image.html', {'image': image})

def apply_filter(request, filter_type, image_id):  # make sure the filter_type is passed in
    if request.method == 'POST':
        try:
            image = get_object_or_404(Image, id=image_id)
            
            from io import BytesIO
            

            file_content = image.image.read()
            img = PILImage.open(BytesIO(file_content))
            
            if filter_type == 'gray':
                filtered_img = ImageOps.grayscale(img)
                filtered_img = filtered_img.convert('RGB')
            elif filter_type == 'blur':
                filtered_img = img.filter(ImageFilter.GaussianBlur(radius=2))
            elif filter_type == 'edge':
                filtered_img = img.filter(ImageFilter.FIND_EDGES)
                filtered_img = filtered_img.convert('RGB')
            elif filter_type == 'solar':
                filtered_img = ImageOps.solarize(img, threshold=128)
            else:
                return JsonResponse({'success': False, 'error': 'not accepted'})
            
            output = BytesIO()
            filtered_img.save(output, format='JPEG')
            output.seek(0)
            
            from django.core.files.base import ContentFile
            image.image.save(os.path.basename(image.image.name), ContentFile(output.getvalue()), save=True)
            
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
        image.delete()
        return redirect('image_list')
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
