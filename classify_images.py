import os
import shutil
import tqdm
import utils

# 디렉토리 설정
config = utils.load_config()

# 이미지 파일명 가져오기
selection_image_names = [os.path.split(path)[-1] for path in utils.get_image_path(config['selection_dir'])]

# 4개 항목
items = ['input_image', 'groundtruth', 'conventional', 'proposed']
for item in items:
    os.makedirs(os.path.join(config['selection_dir'], item), exist_ok=True)

# 선별된 이미지들의 원본 파일을 분류하여 저장
for filename in tqdm.tqdm(selection_image_names):
    for item in items:
        shutil.copy2(os.path.join(config['root'], item, filename),
                     os.path.join(config['selection_dir'], item))
