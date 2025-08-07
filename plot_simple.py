import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
csv_file = 'simple.csv'
df = pd.read_csv(csv_file)

# Extract x and y values
x = df['com_1']
y = df['com_2']

# Create the plot
# plt.plot(x, y)

# plt.plot(x,y, color='gray', linewidth=0.5)
idx0 = 0
num_per_plot = 20
num_per_plot = 100
N = int(len(x)/num_per_plot)
print("N= ",N)
for idx in range(N):
    plt.plot(x[idx0:idx0+num_per_plot],y[idx0:idx0+num_per_plot], color='gray', linewidth=0.5)
    idx0 += 100
#plt.plot(x,y, '.',color='gray', markersize=1)

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
#plt.title('Persistent cell migration - N runs')
plt.title(csv_file)

# Display the plot
#plt.xlim(40, 800)
plt.ylim(25, 75)
plt.show()
