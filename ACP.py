import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#July Data
x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
y1 = [12,15,11,9,1,9,21]

df_july = pd.DataFrame({"Day":x, "New Births":y1})
print(df_july)

#July line plot
plt.title("Birth rate data of July")
plt.plot(x,y1,linestyle='dashed', marker='D', linewidth=4, color='red')
plt.xlabel("Day")
plt.ylabel("New Births")
plt.show()

#August data
y2 = [17,5,2,11,1,8,29]
df_august = pd.DataFrame({"Day":x, "New Births":y2})
print(df_august)

#August line plot
plt.title("Birth rate data of August")
plt.plot(x,y2,linestyle='dotted', marker='o', linewidth=3, color='green')
plt.xlabel("Day")
plt.ylabel("New Births")
plt.show()

#Comparing the two
plt.title("July vs August")
plt.plot(x,y1,linestyle='dashed', marker='D', linewidth=4, color='red')
plt.plot(x,y2,linestyle='dotted', marker='o', linewidth=3, color='green')
plt.xlabel("Day")
plt.ylabel("New Births")
plt.show()

#Solving y=6*2+x+1
x_vals=np.arange(1,11)
y_vals=6*x_vals**2+x_vals+1
plt.title("y=6x^2+x+1 for x=1 to 10")
plt.plot(x_vals,y_vals)
plt.xlabel("x")
plt.ylabel("y")
plt.show()