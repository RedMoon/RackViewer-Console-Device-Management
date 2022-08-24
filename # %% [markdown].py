# %% [markdown]
# # График
# 

# %% [markdown]
# $$
# \int\limits_a^b f(x) dx = F(b) - F(a)
# $$
# 
# 
# 

# %%

from matplotlib import pyplot as plt
import numpy as np


%matplotlib inline

x = np.arange(-10, 10, 1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

plt.figure(figsize=[9, 7])

plt.title('%matplotlib inline function\'s magic', fontsize=18)
plt.plot(x, y1, 'r--', linewidth=2, label='sin()')
plt.plot(x, y2, 'b-.', linewidth=2, label='cos()')
plt.plot(x, y3, 'g:', linewidth=2, label='tan()')

plt.axvline(x=0, color='black')
plt.axhline(y=0, color='black')

plt.xlabel('x-axis', fontsize=15)
plt.ylabel('y-axis', fontsize=15)
plt.legend(fontsize=15)


