import os
import shutil
from tqdm import tqdm
import json


class AddLabelFolder:
    def __init__(self, src_label_folder, label_folder):
        self.src_label_folder = src_label_folder
        self.dest_label_folder = src_label_folder + '_body-80'
        self.label_folder = label_folder

        if not os.path.exists(self.dest_label_folder):
            os.makedirs(self.dest_label_folder)

    def run(self):
        print('copy current labels')
        for file in tqdm(os.listdir(self.src_label_folder)):
            if file.lower().endswith('.json'):
                src_label = self.src_label_folder + '/' + file
                dest_label = self.dest_label_folder + '/' + file
                shutil.copyfile(src_label, dest_label)

        print('add labels')
        for folder in os.listdir(self.label_folder):
            for file in tqdm(os.listdir(self.label_folder + '/' + folder)):
                label = self.dest_label_folder + '/' + file + '.json'
                json_file = open(label, 'r')
                data = json.load(json_file)
                json_file.close()
                data['labels']['body'] = int(folder)
                a_file = open(label, 'w')
                json.dump(data, a_file)
                a_file.close()

    def print_summary(self):
        print()
        print('Summary:')
        print('Labels copied from {} to {}.'.format(self.src_label_folder, self.dest_label_folder))

    def get_dest_folder(self):
        return self.dest_label_folder


if __name__ == '__main__':
    add_label_folder = AddLabelFolder('C:/Users/Florian/Desktop/cars/labels',
                                      'C:/Users/Florian/Desktop/cars/training/body_results_2_80-percent')
    add_label_folder.run()
    add_label_folder.print_summary()
