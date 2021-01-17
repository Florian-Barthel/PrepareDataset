import os
from PIL import Image
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt


class AspectRatio:
    def __init__(self, src_folder):
        self.src_folder = src_folder
        self.allowed_formats = (".jpg", ".jpeg", ".png")
        self.hist = None

    def generate_hist(self, num_bins, interval=(1.0, 2.0)):
        ratios = []
        avg_ratio = 0
        counter = 0
        # hist_y = np.zeros(num_bins, dtype='uint')
        # bin_scale = float(num_bins) / (interval[2] - interval[1])
        for file in tqdm(os.listdir(self.src_folder)):
            if file.lower().endswith(self.allowed_formats):
                src_img_path = self.src_folder + '/' + file
                img = Image.open(src_img_path)
                w, h = img.size
                ratio = w / h
                ratios.append(ratio)
                avg_ratio += w / h
                counter += 1
                # bin_index = int(ratio * bin_scale)
                # hist_y[bin_index] += 1
        # hist_x = np.linspace(interval[0], interval[1], num_bins)
        # plt.hist(hist_x, hist_y)
        print('avg:', avg_ratio / counter)
        print('max:', max(ratios))
        plt.hist(ratios, bins=num_bins)
        plt.title("Aspect Ratios")
        plt.xlabel("width / height")
        plt.xticks(np.arange(1, 2, 0.1))
        plt.ylabel("frequency")
        plt.show()


if __name__ == '__main__':
    aspect_ratio = AspectRatio('C:/Users/Florian/Desktop/cars/images_big')
    aspect_ratio.generate_hist(50)
