import os
from PIL import Image
from tqdm import tqdm


class Resize:
    def __init__(self, src_folder, width):
        self.src_folder = src_folder
        self.dest_folder = src_folder + '_resize-' + str(width)
        self.counter = 0
        self.allowed_formats = ".jpg"
        self.width = width

        if not os.path.exists(self.dest_folder):
            os.makedirs(self.dest_folder)

    def run(self):
        for file in tqdm(os.listdir(self.src_folder)):
            if file.lower().endswith(self.allowed_formats):
                src_img_path = self.src_folder + '/' + file

                img = Image.open(src_img_path)
                w, h = img.size
                current_ratio = float(h / w)
                height = int(current_ratio * self.width)
                img = img.resize((self.width, height), Image.ANTIALIAS)
                img.save(self.dest_folder + '/' + file)

    def print_summary(self):
        print()
        print('Summary:')
        print('Resize images')
        print('Files copied from {} to {}.'.format(self.src_folder, self.dest_folder))
        print('Number of images:', str(self.counter))

    def get_dest_folder(self):
        return self.dest_folder


if __name__ == '__main__':
    resize = Resize('C:/Users/Florian/Desktop/cars/images_big_crop-multiple', 512)
    resize.run()
