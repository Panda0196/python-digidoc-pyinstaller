import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def asice_path(file_name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

print("abs dirname:", os.path.dirname(os.path.abspath(__file__)))
print("Digidoc asukoht:", resource_path('digidoc-tool.exe'))

failid = '\"' + resource_path('digidoc-tool.exe') \
    + '\" open "' + asice_path('TEST2.asice') \
    + '" --extractAll="' + os.path.dirname(os.path.abspath(__file__)) +'"'

print(failid)
print(os.popen(failid).read())

input("Press Enter to exit...")
