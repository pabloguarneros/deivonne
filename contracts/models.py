from django.db import models
from PIL import Image


def contract_image_directory_path(instance, filename): 
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'contract_poster/{0}/{1}'.format(instance.pk, f"{filename}") 

class SmartContract(models.Model): 

    def __str__(self):
        return self.poster.path.rsplit('/', 1)[-1]
    
    title = models.CharField(max_length=140, blank=True)
    poster = models.ImageField(upload_to=contract_image_directory_path)
    short_description = models.CharField(max_length=140, blank=True)
    public_key = models.CharField(max_length=140, blank=True)

    class SectorArea(models.IntegerChoices):
        EDUCATION = 0
        SUSTAINABILITY = 1
        HEALTHSERVICES = 2

    sector = models.IntegerField(choices=SectorArea.choices, default=None, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.poster.path)

        if img.height > 450 or img.width > 450:
            new_img = (450, 450)
            img.thumbnail(new_img)
            img = img.convert('RGB') #convert transparency to new image!
            img.save(self.poster.path)  # saving image at the same path
