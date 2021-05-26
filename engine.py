# from __future__ import division
import uuid
import numpy as np
from PIL import Image
from scipy import interpolate
import matplotlib.pyplot as plt


def draw(tck, img):
    x = np.linspace(0, 1, num=100, endpoint=True)
    with Image.open(img).convert('RGBA') as img:
        plt.imshow(img, aspect='auto', zorder=0)
    xnew, ynew = interpolate.splev(x, tck=tck, der=0)
    plt.plot(xnew, ynew, color='red', zorder=1)
    plt.axis('off')
    try:
        name = uuid.uuid4().hex
        plt.savefig('{}/{}'.format('img/generates/', name), bbox_inches='tight', pad_inches=0)
        plt.close()
        return('{}/{}.png'.format('img/generates', name))
    except Exception:
        return(False)
