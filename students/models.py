from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from django.urls import reverse

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100, unique=True) # unique=True to make sure that the student_id is unique
    qr_code = models.ImageField(upload_to='qr_codes', blank=True) # blank=True to make the field optional

    def save(self, *args, **kwargs): # *args and **kwargs allow us to pass a variable number of arguments to a function
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.student_id) # add student_id to the qr code
        qr.make(fit=True) # make the qr code fit the image

        img = qr.make_image(fill_color="black", back_color="white") # create the qr code image
        buffer = BytesIO() # create a BytesIO object
        img.save(buffer) # save the qr code image to the BytesIO object
        filename = f'qr_code-{self.name}_qrcode.png' # create a filename for the qr code image
        self.qr_code.save(filename, File(buffer), save=False) # save the qr code image to the qr_code field of the Student model
        super().save(*args, **kwargs) # call the save method of the parent class

    def __str__(self): # return the name of the student
        return self.name