from django.db import models

import subprocess


class Files(models.Model):
    # doc = models.TextField()
    File_name = models.ImageField(upload_to='Files/')
    print(File_name)


# path="Nitika.docx"
# o_path="./"
# output = subprocess.check_output(['libreoffice', '--convert-to', 'pdf' ,path])
# print(output)
