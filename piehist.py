#PIE CHART

import matplotlib.pyplot as plt
subjects=["Physics","Chemistry","Maths"."AI"."Python"]
marks=[89,90,97,78,80]
plt.pie(marks,labels=subjects,autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()


#HISTAGRAM CHART

import matplotlib.pyplot as plt
marks=[90,80,70,60,50,40]
plt.hist(marks)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Histagram of marks")
plt.show()
