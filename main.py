from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

from pipeline import Pipeline

from file_structure.flat_structure import FlatStructure
from file_structure.rename import Rename
from file_structure.copy import Copy
from file_structure.split_images_labels import SplitImagesLabels

from filter.ratio import FilterRatio
from filter.warnings import FilterWarnings

from modify_images.convert_to_jpg import ConvertJPG
from modify_images.crop import Crop
from modify_images.resize import Resize
from modify_images.pad import Pad

from modify_labels.add_label_folder import AddLabelFolder
from modify_labels.add_label_dict import AddLabelDict

size = [256, 160]
ratio = size[0] / size[1]
pad_height = 256

dataset = 'C:/Users/Florian/Desktop/cars_rename_jpg_crop_resize_pad'
labels = 'C:/Users/Florian/Desktop/orientation_results'
add_label = AddLabelFolder(dataset, labels)

# rename = Rename(dataset)
# convert_jpg = ConvertJPG(rename.get_dest_folder())
# crop = Crop(convert_jpg.get_dest_folder(), ratio=ratio)
# resize = Resize(crop.get_dest_folder(), size=size)
# pad = Pad(resize.get_dest_folder(), pad_height=pad_height)

task_list = [add_label]

pipeline = Pipeline(task_list=task_list)
pipeline.run()
