import os
import shutil
from PIL import Image
from tqdm import tqdm
import json


class CropMultiple:
    def __init__(self, src_img_folder, src_label_folder, ratios=(1.2, 1.4, 1.6, 1.8, 2.0)):
        self.src_img_folder = src_img_folder
        self.src_label_folder = src_label_folder
        self.dest_img_folder = src_img_folder + '_crop-multiple'
        self.dest_label_folder = src_label_folder + '_crop-multiple'
        self.counter = 0
        self.allowed_formats = ".jpg"
        self.ratios = ratios

        if not os.path.exists(self.dest_img_folder):
            os.makedirs(self.dest_img_folder)

        if not os.path.exists(self.dest_label_folder):
            os.makedirs(self.dest_label_folder)

    def run(self):
        for file in tqdm(os.listdir(self.src_img_folder)):
            if file.lower().endswith(self.allowed_formats):
                src_img_path = self.src_img_folder + '/' + file
                img = Image.open(src_img_path)

                w, h = img.size
                current_ratio = w / h
                closest_ratio = min(self.ratios, key=lambda x: abs(x - current_ratio))
                ratio_index = self.ratios.index(closest_ratio)
                if w > int(h * closest_ratio):
                    new_w = int(h * closest_ratio)
                    new_h = h
                else:
                    new_w = w
                    new_h = int(w / closest_ratio)

                w_diff = w - new_w
                h_diff = h - new_h

                x1 = int(w_diff / 2)
                x2 = new_w + x1
                y1 = int(h_diff / 2)
                y2 = new_h + y1
                img = img.crop((x1, y1, x2, y2))

                img.save(self.dest_img_folder + '/' + file)

                src_label = self.src_label_folder + '/' + file + '.json'
                if os.path.exists(src_label):
                    dest_label = self.dest_label_folder + '/' + file + '.json'
                    shutil.copyfile(src_label, dest_label)

                    json_file = open(dest_label, 'r')
                    data = json.load(json_file)
                    json_file.close()


                    data['labels']['ratio'] = ratio_index

                    a_file = open(dest_label, 'w')
                    json.dump(data, a_file)
                    a_file.close()

    def print_summary(self):
        print()
        print('Summary:')
        print('Crop images to desired ratio')
        print('Images copied from {} to {}.'.format(self.src_img_folder, self.dest_img_folder))
        print('Labels copied from {} to {}.'.format(self.src_label_folder, self.dest_label_folder))
        print('Number of images:', str(self.counter))

    def get_dest_folder(self):
        return self.dest_img_folder, self.dest_label_folder


if __name__ == '__main__':
    crop_multiple = CropMultiple('C:/Users/Florian/Desktop/cars/images_big', 'C:/Users/Florian/Desktop/cars/labels_body-80')
    crop_multiple.run()
