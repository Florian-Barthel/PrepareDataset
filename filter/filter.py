import os
import shutil


class Filter:
    def __init__(self, src_folder, dest_folder):
        self.src_folder = src_folder
        self.dest_folder = dest_folder
        self.remove_folder = dest_folder + '_remove'
        self.num_kept = 0
        self.num_removed = 0
        self.allowed_formats = (".jpg", ".jpeg", ".png")

        if not os.path.exists(self.dest_folder):
            os.makedirs(self.dest_folder)

        if not os.path.exists(self.remove_folder):
            os.makedirs(self.remove_folder)

    def run(self):
        pass

    def copy(self, file, dest):
        src_img = self.src_folder + '/' + file
        dest_img = dest + '/' + file

        src_label = self.src_folder + '/' + file + '.json'
        dest_label = dest + '/' + file + '.json'

        shutil.copyfile(src_img, dest_img)
        if os.path.exists(src_label):
            shutil.copyfile(src_label, dest_label)

    def keep(self, file):
        self.copy(file, self.dest_folder)
        self.num_kept += 1

    def remove(self, file):
        self.copy(file, self.remove_folder)
        self.num_removed += 1

    def print_summary(self):
        print()
        print('Summary:')
        print('Files copied from {} to {}.'.format(self.src_folder, self.dest_folder))
        print('Number of removed images:', str(self.num_removed))
        print('Number of kept images:', str(self.num_kept))

    def get_dest_folder(self):
        return self.dest_folder