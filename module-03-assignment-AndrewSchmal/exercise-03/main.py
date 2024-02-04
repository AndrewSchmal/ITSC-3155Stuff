import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Display basic statistics using the info method
print(df.info())

# Plot x versus y columns
plt.plot(df['x'], df['y'])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Dataset: X versus Y')
plt.show()



# i originally just used the following git bash command to add them all individually before i remembered you probably wanted to edit the vm into ignore
# git add exercise-03/data.csv exercise-03/main.py exercise-03/requirements.txt

