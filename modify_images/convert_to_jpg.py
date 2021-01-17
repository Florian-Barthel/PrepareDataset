import os
import shutil
from PIL import Image
from tqdm import tqdm


class ConvertJPG:
    def __init__(self, src_folder):
        self.src_folder = src_folder
        self.dest_folder = src_folder + '_jpg'
        self.counter = 0
        self.allowed_formats = (".jpg", ".jpeg", ".png")

        if not os.path.exists(self.dest_folder):
            os.makedirs(self.dest_folder)

    def run(self):
        for file in tqdm(os.listdir(self.src_folder)):
            if file.lower().endswith(self.allowed_formats):
                src_img_path = self.src_folder + '/' + file
                img = Image.open(src_img_path)
                if not img.mode == 'RGB':
                    img = img.convert('RGB')
                new_file_name = file.lower().split('.')[0] + '.jpg'
                img.save(self.dest_folder + '/' + new_file_name)

                src_label = self.src_folder + '/' + file + '.json'
                if os.path.exists(src_label):
                    dest_label = self.dest_folder + '/' + new_file_name + '.json'
                    shutil.copyfile(src_label, dest_label)

    def print_summary(self):
        print()
        print('Summary:')
        print('Convert images to jpg')
        print('Files copied from {} to {}.'.format(self.src_folder, self.dest_folder))
        print('Number of images:', str(self.counter))

    def get_dest_folder(self):
        return self.dest_folder
