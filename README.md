# Extract text from Image
-------------------------

It will recognize and read the text present in images by electronically extracting text from images or any documents like PDF.

---

# Run the script
----------------

```
python3 script.py <arg1>
```
where ```arg1``` is the path of the image.
The result will be printed in a folder within ```output```

---

# Requirements
--------------

### Dependencies 

```pip3 install -r requirements.txt```

### Tesseract

on Linux: ```sudo apt-get install tesseract-ocr```

on mac: ```brew install tesseract```

on Windows:
 - Download the latest released version of the Windows installer for Tesseract.
 - Run the executable file to install. It will install to C:\Program Files (x86)\Tesseract OCR.
 - Make sure your TESSDATA_PREFIX environment variable is set correctly:
