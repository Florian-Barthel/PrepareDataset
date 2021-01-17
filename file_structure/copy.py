import os
import shutil
from tqdm import tqdm


class Copy:
    def __init__(self, src_folder):
        self.src_folder = src_folder
        self.dest_folder = src_folder + '_copy'
        self.counter = 0
        self.allowed_formats = (".jpg", ".jpeg", ".png")

        if not os.path.exists(self.dest_folder):
            os.makedirs(self.dest_folder)

    def run(self):
        for file in tqdm(os.listdir(self.src_folder)):
            if file.lower().endswith(self.allowed_formats):
                src_img = self.src_folder + '/' + file
                dest_img = self.dest_folder + '/' + file
                shutil.copyfile(src_img, dest_img)
                self.counter += 1

    def print_summary(self):
        print()
        print('Summary:')
        print('Files copied')
        print('Files copied from {} to {}.'.format(self.src_folder, self.dest_folder))
        print('Number of images:', str(self.counter))

    def get_dest_folder(self):
        return self.dest_folder
