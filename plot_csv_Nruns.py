import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
# df = pd.read_csv('save_2runs.csv')
# df = pd.read_csv('save.csv')

csv_file = 'model4_TF.csv'
csv_file = 'model4_physicell.csv'
csv_file = 'pc_combined_tracks.csv'
csv_file = 'save.csv'
csv_file = 'pc_all.csv'
csv_file = 'pc_bias025.csv'
csv_file = 'pc_bias.csv'
csv_file = 'pc_bias_05.csv'
df = pd.read_csv(csv_file)

# Extract x and y values
x = df['com_1']
y = df['com_2']

# Create the plot
# plt.plot(x, y)

# plt.plot(x,y, color='gray', linewidth=0.5)
idx0 = 0
N = int(len(x)/100)
print("N= ",N)
for idx in range(N):
    plt.plot(x[idx0:idx0+100],y[idx0:idx0+100], color='gray', linewidth=0.5)
    idx0 += 100

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
#plt.title('Persistent cell migration - N runs')
plt.title(csv_file)

# Display the plot
plt.xlim(40, 800)
plt.ylim(25, 75)
plt.show()
