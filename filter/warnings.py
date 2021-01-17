from tqdm import tqdm
import os
from PIL import Image
import warnings
from filter.filter import Filter


class FilterWarnings(Filter):
    def __init__(self, src_folder):
        dest_folder = src_folder + '_warnings'
        super().__init__(src_folder, dest_folder)

    def run(self):
        for file in tqdm(os.listdir(self.src_folder)):
            if file.lower().endswith(self.allowed_formats):
                with warnings.catch_warnings() as my_warning:
                    warnings.simplefilter('error', UserWarning)
                    try:
                        src_img_path = self.src_folder + '/' + file
                        img = Image.open(src_img_path)
                        self.keep(file)
                    except:
                        self.remove(file)
