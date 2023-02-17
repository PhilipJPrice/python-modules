from PIL import Image
from zipsearch2 import ZipProcessor

class ScaleZip(ZipProcessor):
    def process_files(self):
        '''Scale each image in the directory to 640x480'''
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((640, 480))
            scaled.save(filename)

if __name__ == "__main__":
    ScaleZip(*sys.argv[1:4]).process_zip()
