import os
import shutil
from PIL import Image
from tqdm import tqdm


class Pad:
    def __init__(self, src_folder, pad_height):
        self.src_folder = src_folder
        self.dest_folder = src_folder + '_pad'
        self.counter = 0
        self.allowed_formats = ".jpg"
        self.pad_height = pad_height

        if not os.path.exists(self.dest_folder):
            os.makedirs(self.dest_folder)

    def run(self):
        for file in tqdm(os.listdir(self.src_folder)):
            if file.lower().endswith(self.allowed_formats):
                src_img_path = self.src_folder + '/' + file
                img = Image.open(src_img_path)
                width, height = img.size

                pad_img = Image.new(img.mode, (width, self.pad_height), (0, 0, 0))
                pad_img.paste(img, (0, (width - height) // 2))
                pad_img.save(self.dest_folder + '/' + file)


    def print_summary(self):
        print()
        print('Summary:')
        print('Pad images')
        print('Files copied from {} to {}.'.format(self.src_folder, self.dest_folder))
        print('Number of images:', str(self.counter))

    def get_dest_folder(self):
        return self.dest_folder

if __name__ == '__main__':
    pad = Pad('C:/Users/Florian/Desktop/cars/images_big_crop-multiple_resize-256', 256)
    pad.run()
