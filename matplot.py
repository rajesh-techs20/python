import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,4,9,16,25]

plt.plot(x,y)
plt.xlabel("Numbers")
plt.ylabel("Square of numbers")
plt.show()

Students=["Rajesh","Nandan","Adish"]
marks=[89,70,98]
plt.bar(Students,marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

Marks=[3,5,4,8,19,13,20,15,99,67,45,23,88,33,67]
plt.hist(Marks)
plt.ylabel("Number of students")
plt.show()

Fruits=["Apple","Mango","Orange","Pinaple","Pappaya"]
quantities=[20,56,89,90,48]

plt.pie(quantities,labels=Fruits,autopct='%1.2f%%')
plt.show()

