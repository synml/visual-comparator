import glob
import os
import matplotlib.pyplot as plt
import yaml


# 설정파일 불러오기
def load_config():
    with open('config.yaml') as f:
        config = yaml.safe_load(f)
    return config


# 이미지 경로를 가져옴
def get_image_path(root: str, sub_dir: str):
    paths = glob.glob(os.path.join(root, sub_dir, '*'))
    paths.sort()
    return paths


# plot을 제작
def make_plot(titles: list, images: list, save_plot: str = None, show_plot=False):
    fig, axs = plt.subplots(2, 2)
    for ax in axs.reshape(4):
        ax.set_title(titles.pop(0))
        ax.imshow(images.pop(0))

    if save_plot is not None:
        plt.savefig(save_plot)
    if show_plot:
        plt.show()
    plt.close()


# matplotlib rcParams를 설정
def set_matplotlib_rcparams():
    plt.rcParams['figure.figsize'] = (18.5, 9.8)
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['xtick.bottom'] = False
    plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['ytick.left'] = False
    plt.rcParams['ytick.labelleft'] = False
