#API Introduction: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.pie

import matplotlib.pyplot as plt

labels = 'A', 'B', 'C', 'D', 'E', 'F', 'G'
sizes = [20, 45, 68, 98, 60, 28, 99]
explode = (0, 0.1, 0, 0, 0, 0, 0)

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%.2f%%', shadow=True, startangle=90)
fig.set_size_inches(8, 8)
plt.show()