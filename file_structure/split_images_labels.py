import os
import shutil
from tqdm import tqdm


class SplitImagesLabels:
    def __init__(self, src_folder):
        self.src_folder = src_folder
        self.dest_img_folder = src_folder + '_images'
        self.dest_label_folder = src_folder + '_labels'
        self.img_counter = 0
        self.label_counter = 0
        self.allowed_formats = (".jpg", ".jpeg", ".png")

        if not os.path.exists(self.dest_img_folder):
            os.makedirs(self.dest_img_folder)
        if not os.path.exists(self.dest_label_folder):
            os.makedirs(self.dest_label_folder)

    def run(self):
        for file in tqdm(os.listdir(self.src_folder)):
            if file.lower().endswith(self.allowed_formats):
                src_img = self.src_folder + '/' + file
                dest_img = self.dest_img_folder + '/' + file
                shutil.copyfile(src_img, dest_img)
                self.img_counter += 1

        for file in tqdm(os.listdir(self.src_folder)):
            if file.lower().endswith('.json'):
                src_label = self.src_folder + '/' + file
                dest_label = self.dest_label_folder + '/' + file
                shutil.copyfile(src_label, dest_label)
                self.label_counter += 1

    def print_summary(self):
        print()
        print('Summary:')
        print('Files split into images and labels')
        print('Files copied from {} to {} and {}.'.format(self.src_folder, self.dest_img_folder, self.dest_label_folder))
        print('Number of images:', str(self.img_counter))
        print('Number of labels:', str(self.label_counter))

    def get_dest_folders(self):
        return self.dest_img_folder, self.dest_label_folder


if __name__ == '__main__':
    split = SplitImagesLabels('C:/Users/Florian/Desktop/cars/images_big')
    split.run()
    split.print_summary()
