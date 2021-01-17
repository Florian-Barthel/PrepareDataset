import os
import shutil
from PIL import Image
from tqdm import tqdm


class Crop:
    def __init__(self, src_folder, ratio):
        self.src_folder = src_folder
        self.dest_folder = src_folder + '_crop'
        self.counter = 0
        self.allowed_formats = ".jpg"
        self.ratio = ratio

        if not os.path.exists(self.dest_folder):
            os.makedirs(self.dest_folder)

    def run(self):
        for file in tqdm(os.listdir(self.src_folder)):
            if file.lower().endswith(self.allowed_formats):
                src_img_path = self.src_folder + '/' + file
                img = Image.open(src_img_path)

                w, h = img.size
                if w > int(h * self.ratio):
                    new_w = int(h * self.ratio)
                    new_h = h
                else:
                    new_w = w
                    new_h = int(w / self.ratio)

                w_diff = w - new_w
                h_diff = h - new_h

                x1 = int(w_diff / 2)
                x2 = new_w + x1
                y1 = int(h_diff / 2)
                y2 = new_h + y1
                img = img.crop((x1, y1, x2, y2))

                img.save(self.dest_folder + '/' + file)
                src_label = self.src_folder + '/' + file + '.json'
                if os.path.exists(src_label):
                    dest_label = self.dest_folder + '/' + file + '.json'
                    shutil.copyfile(src_label, dest_label)

    def print_summary(self):
        print()
        print('Summary:')
        print('Crop images to desired ratio')
        print('Files copied from {} to {}.'.format(self.src_folder, self.dest_folder))
        print('Number of images:', str(self.counter))

    def get_dest_folder(self):
        return self.dest_folder
