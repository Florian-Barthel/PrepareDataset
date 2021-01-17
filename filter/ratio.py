from tqdm import tqdm
import os
from PIL import Image
from filter.filter import Filter


class FilterRatio(Filter):
    def __init__(self, src_folder, min_ratio):
        dest_folder = src_folder + '_ratio'
        super().__init__(src_folder, dest_folder)
        self.min_ratio = min_ratio

    def run(self):
        for file in tqdm(os.listdir(self.src_folder)):
            if file.lower().endswith(self.allowed_formats):
                src_img_path = self.src_folder + '/' + file
                img = Image.open(src_img_path)
                w, h = img.size
                if w / h > self.min_ratio:
                    self.keep(file)
                else:
                    self.remove(file)
