import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[1,4,9,16,25]

plt.plot(x,y)

plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()


#BAR GRAPH

import matplotlib.plotpy as plt

students=["Adish","Rajesh","Nandan"]
marks=[12,16,10]
plt.bar(students,marks)

plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
