import os
import shutil
from tqdm import tqdm
import json


class AddLabelDict:
    def __init__(self, src_folder, label_folder):
        self.src_folder = src_folder
        self.dest_folder = src_folder + '_label'
        self.counter = 0
        self.allowed_formats = (".jpg", ".jpeg", ".png")
        self.label_folder = label_folder

        if not os.path.exists(self.dest_folder):
            os.makedirs(self.dest_folder)

    def run(self):
        for file in tqdm(os.listdir(self.src_folder)):
            if file.lower().endswith(self.allowed_formats):
                src_img = self.src_folder + '/' + file
                dest_img = self.dest_folder + '/' + file
                shutil.copyfile(src_img, dest_img)
                self.counter += 1

                src_label = self.src_folder + '/' + file + '.json'
                if os.path.exists(src_label):
                    dest_label = self.dest_folder + '/' + file + '.json'
                    shutil.copyfile(src_label, dest_label)

        for file in tqdm(os.listdir(self.dest_folder)):
            if file.lower().endswith(self.allowed_formats):
                label = self.dest_folder + '/' + file + '.json'
                if os.path.exists(label):
                    json_file = open(label, 'r')
                    data = json.load(json_file)
                    json_file.close()

                    data['labels']['orientation'] = int(folder)

                    a_file = open(label, 'w')
                    json.dump(data, a_file)
                    a_file.close()

    def print_summary(self):
        print()
        print('Summary:')
        print('Files copied and added label')
        print('Files copied from {} to {}.'.format(self.src_folder, self.dest_folder))
        print('Number of images:', str(self.counter))

    def get_dest_folder(self):
        return self.dest_folder
