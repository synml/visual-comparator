import os
from PIL import Image
import tqdm
import utils

# 디렉토리 설정
root = 'images'
save_dir = 'output'
os.makedirs(save_dir, exist_ok=True)

# 이미지 경로 가져오기
paths_input_image = utils.get_image_path(root, 'input_image')
paths_groundtruth = utils.get_image_path(root, 'groundtruth')
paths_conventional = utils.get_image_path(root, 'conventional')
paths_proposed = utils.get_image_path(root, 'proposed')
assert len(paths_input_image) == len(paths_groundtruth) == len(paths_conventional) == len(paths_proposed)

# matplotlib rcParams 설정
utils.set_matplotlib_rcparams()

# plot 제작 후 저장
zip_iter = zip(paths_input_image, paths_groundtruth, paths_conventional, paths_proposed)
for paths in tqdm.tqdm(zip_iter, total=len(paths_input_image)):
    input_image = Image.open(paths[0])
    groundtruth = Image.open(paths[1])
    conventional = Image.open(paths[2])
    proposed = Image.open(paths[3])
    input_image = input_image.resize(groundtruth.size)
    assert input_image.size == groundtruth.size == conventional.size == proposed.size

    image_name = os.path.split(paths[0])[-1]
    titles = ['Input image ({})'.format(image_name), 'Groundtruth', 'Conventional', 'Proposed']
    images = [input_image, groundtruth, conventional, proposed]
    utils.make_plot(titles, images, os.path.join(save_dir, image_name))
