from django.db import models
from PIL import Image


def contract_image_directory_path(instance, filename): 
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'contract_poster/{0}/{1}'.format(instance.pk, f"{filename}") 

class SmartContract(models.Model): 

    '''
    IMPORTANT!! Hash should be changed to models.UUIDField to prevent duplicate profiles for one specific contract!
    However, for testing purposes (given association with SDGs proxies), we allow duplicates.
    '''

    def __str__(self):
        return self.title

    title = models.CharField(max_length=140, blank=True)
    short_description = models.TextField()
    hash = models.CharField(max_length=140, blank=True, default="KT1Puc9St8wdNoGtLiD2WXaHbWU7styaxYhD")

    poster = models.ImageField(upload_to=contract_image_directory_path,blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class SectorArea(models.IntegerChoices):
        NOPOVERTY = 0
        ZEROHUNGER = 1
        GOODHEALTH = 2
        QUALITYEDUCATION = 3
        GENDEREQUALITY = 4
        CLEANWATER = 5
        AFFORDABLEENERGY = 6
        DECENTWORK = 7
        INDUSTRYINNOVATION = 8
        REDUCEINEQUALITY = 9
        SUSTAINABLECITIES = 10
        RESPONSIBLECONSUMPTION = 11
        CLIMATEACTION = 12
        BELOWWATER = 13
        ONLAND = 14
        PEACEFULINSTITUIONS = 15
        PARTNERSHIP = 16

    sector = models.IntegerField(choices=SectorArea.choices, default=15)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.poster != "":
            img = Image.open(self.poster.path)

            if img.height > 450 or img.width > 450:
                new_img = (450, 450)
                img.thumbnail(new_img)
                img = img.convert('RGB') #convert transparency to new image!
                img.save(self.poster.path)  # saving image at the same path
