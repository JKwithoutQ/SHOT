import os
from typing import Optional


def image_list(path: str, pre_path: Optional[str] = None, save_path: Optional[str] = None) -> None:
    """ lab from 0 to length-1
    """
    with open(save_path, 'w') as f:
        cate_lst = sorted(os.listdir(path))
        for lab, cate in enumerate(cate_lst):
            for img in os.listdir(os.path.join(path, cate)):
                if pre_path is None:
                    img_path = os.path.join(path, cate, img)
                else:
                    img_path = os.path.join(pre_path, path, cate, img)
                f.write(f'{img_path} {lab}\n')
    print(f'finish save path: {save_path}')


if __name__ == '__main__':
    image_list(path='./data/office-home/Art', save_path='./data/office-home/Art_list.txt')
    image_list(path='./data/office-home/Clipart', save_path='./data/office-home/Clipart_list.txt')
    image_list(path='./data/office-home/Product', save_path='./data/office-home/Product_list.txt')
    image_list(path='./data/office-home/RealWorld', save_path='./data/office-home/RealWorld_list.txt')
