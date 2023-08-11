import numpy as np
import matplotlib.pyplot as plt

size = 3
a = [0.7400,0.7300,0.7000]
b = [0.7305,0.7195,0.6925]
c = [0.7407,0.7256,0.6855]

x = np.arange(size)
total_width,n=0.8,3
width = total_width/n

x = x-(total_width-width)/2

plt.bar(x,a,width=width,label='$mask$=0.1')
plt.bar(x+width,b,width=width,label='$mask$=0.3')
plt.bar(x+2*width,c,width=width,label='$mask$=0.5')
group_labels = ['$\mu=0.2$', '$\mu=0.4$', '$\mu=0.6$']
plt.xticks(x+width, group_labels, fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')
# plt.title("example", fontsize=12, fontweight='bold')  # 默认字体大小为12
plt.xlabel("Ratio of noise samples", fontsize=13, fontweight='bold')
plt.ylabel("Accuracy", fontsize=13, fontweight='bold')

plt.ylim(0.5, 0.8)
plt.legend()
plt.show()