#PIE CHART

import matplotlib.pyplot as plt
subjects=["Physics","Chemistry","Maths"."AI"."Python"]
marks=[89,90,97,78,80]
plt.pie(marks,labels=subjects,autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()
