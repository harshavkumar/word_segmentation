# -*- coding: utf-8 -*-
"""
Helper functions for ocr project
"""
import numpy as np
import cv2


SMALL_HEIGHT = 800


def implt(img, cmp=None, t=''):
    """Show image using plt."""
    cv2.namedWindow('', cv2.WINDOW_NORMAL)
    cv2.imshow('', img)
    cv2.waitKey(0)


def resize(img, height=SMALL_HEIGHT, allways=False):
    """Resize image to given height."""
    # print(img.shape[1], img.shape[0])
    if (img.shape[0] > height or allways):
        rat = height / img.shape[0]
        return cv2.resize(img, (int(rat * img.shape[1]), height))
    
    return img


def ratio(img, height=SMALL_HEIGHT):
    """Getting scale ratio."""
    return img.shape[0] / height


def img_extend(img, shape):
    """Extend 2D image (numpy array) in vertical and horizontal direction.
    Shape of result image will match 'shape'
    Args:
        img: image to be extended
        shape: shape (touple) of result image
    Returns:
        Extended image
    """
    x = np.zeros(shape, np.uint8)
    x[:img.shape[0], :img.shape[1]] = img
    return x