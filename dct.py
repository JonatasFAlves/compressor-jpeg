import numpy as np
import cv2


def dct_from_ycrcb_blocks(yblocks, cr_blocks, cb_blocks):
    i = [dct_from_blocks(i) for i in [yblocks, cr_blocks, cb_blocks]]
    return np.asarray(i)


# TODO melhorar este método. Talvez usar list comprehension?
def dct_from_blocks(image_blocks):
    dct_blocks = []

    for block in image_blocks:
        imf = np.float32(block)/255.0  # float conversion/scale
        dct_blocks.append(cv2.dct(imf))

    return dct_blocks


def idct_from_ycrcb_dct_blocks(yblocks, cr_blocks, cb_blocks):
    i = [idct_from_blocks(i) for i in [yblocks, cr_blocks, cb_blocks]]
    return np.asarray(i)


# TODO melhorar este método. Talvez usar list comprehension?
def idct_from_blocks(dct_blocks):
    idct_blocks = []

    for block in dct_blocks:
        idct_block = cv2.idct(block)
        idct_blocks.append(np.uint8((idct_block * 255.0)))  # convert back

    return idct_blocks