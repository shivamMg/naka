from io import BytesIO

from PIL import Image
from selenium import webdriver
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile

from .models import Photo


def capture_screenshot(project):
    """Captures screenshot of Project website and saves it as
    project photo. If Project website is not available, then
    project source is used.
    """
    screenshot_url = project.source_link if not project.website_link \
        else project.website_link

    driver = webdriver.PhantomJS()
    driver.set_window_size(1024, 420)
    # Get URL
    driver.get(screenshot_url)
    screenshot = driver.get_screenshot_as_png()

    img = Image.open(BytesIO(screenshot))
    # Crop image
    box = (0, 0, 1024, 420)
    img = img.crop(box)
    # Save image in a buffer and create a content file
    buffer_ = BytesIO()
    img.save(buffer_, 'PNG')
    content_file = ContentFile(buffer_.getvalue())

    # Save content file in memory and pass it to Project photo
    # File is automatically renamed by Django in case of conflicts
    image_file = InMemoryUploadedFile(content_file, None, 'project.png',
                                      'image/png', content_file.tell, None)

    Photo.objects.update_or_create(project=project,
                                   defaults={'image': image_file})
