"""cloud_generator.py
"""
# https://github.com/amueller/word_cloud/tree/master/examples
#!/usr/bin/env python
"""
Using custom colors
===================
Using the recolor method and custom coloring functions.

Adapted From:
    https://github.com/amueller/word_cloud
    name
"""

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os
import random
from wordcloud import WordCloud, STOPWORDS

def grey_color_func(word,
                    font_size,
                    position,
                    orientation,
                    random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

d = os.path.dirname("cloud_generator.py")

# read the mask image
mask_outer = np.array(Image.open(os.path.join(d, "network.png")))
mask_inner = np.array(Image.open(os.path.join(d, "network_reverse.png")))

# text
text = open("network.txt").read()

net_outside = WordCloud(max_words=10000,
                                     mask=mask_outer,
                                     margin=20,
                                     random_state=5).generate(text)

net_inside = WordCloud(max_words=10000,
                                     mask=mask_inner,
                                     margin=1,
                                     random_state=10).generate(text)

# store default colored image
default_colors = net_inside.to_array()
plt.imshow(net_outside.recolor(color_func=grey_color_func, 
                                            random_state=3),
                                            interpolation="bilinear")
net_outside.to_file("net_outside.png")

plt.imshow(net_inside, interpolation="bilinear")
net_inside.to_file("net_inside.png")
