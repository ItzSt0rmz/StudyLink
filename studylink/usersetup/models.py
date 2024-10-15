from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='static\default_profile.jpg', upload_to='profile_images')
    bio = models.TextField(default="Hi!")

    # classes taken
    english1Taken = models.BooleanField(default=False, name = "English 1")
    english2Taken = models.BooleanField(default=False, name="English 2")
    english3Taken = models.BooleanField(default=False, name="English 3")
    english4Taken = models.BooleanField(default=False, name="English 4")
    APlitTaken = models.BooleanField(default=False, name="AP Literature")
    APlangTaken = models.BooleanField(default=False, name="AP Language")

    preAlgebraTaken = models.BooleanField(default=False, name = "Pre-Algebra")
    algebra1Taken = models.BooleanField(default=False, name="Algebra 1")
    algebra2Taken = models.BooleanField(default=False, name="Algebra 2")
    geometryTaken = models.BooleanField(default=False, name="Geometry")
    preCalculusTaken = models.BooleanField(default=False, name="Pre-Calculus")
    calculusABTaken = models.BooleanField(default=False, name="Calculus AB")
    calculusBCTaken = models.BooleanField(default=False, name="Calculus BC")

    APphysics1Taken = models.BooleanField(default=False, name = "AP Physics 1")
    APphysicsCTaken = models.BooleanField(default=False, name="AP Physics C")
    chemTaken = models.BooleanField(default=False, name="Chemistry")
    APchemTaken = models.BooleanField(default=False, name="AP Chemistry")
    bioTaken = models.BooleanField(default=False, name="Biology")
    APbioTaken = models.BooleanField(default=False, name="AP Biology")
    APESTaken = models.BooleanField(default=False, name="AP Environemental Science")
    APpsychTaken = models.BooleanField(default=False, name="AP Psychology")

    # classes for study

    phoneNumber = models.IntegerField(default="0123456789")

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

    def __str__(self):
        return self.user.username

