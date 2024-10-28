import seaborn as sns
import matplotlib.pyplot as plt
import math
import numpy as np
import seaborn.objects

# replace print // for ease
def log(x):
    print(str(x))


dataset = sns.get_dataset_names()
log(dataset)
dataset = sns.load_dataset("diamonds")
log(dataset)
sample_limit = 20000
step = 100

x_axis, y_axis = dataset["carat"][:sample_limit][::step],\
                 dataset["price"][:sample_limit][::step]


sns.set_palette("magma")
sns.jointplot(x=x_axis,
              y=y_axis,
              kind="kde",
              cmap="magma_r",
              fill=True,
              )
plt.show()