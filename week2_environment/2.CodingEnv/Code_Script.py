import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import os.path
#os.environ['RESEARCH_PATH'] = '/Users/chenyidan/homework_dft/week2_environment/2.CodingEnv'
path = os.path.expandvars("$RESEARCH_PATH") + "/Data/data.csv"
print(path)
#path = "$RESEARCH_PATH/Data/data.csv"
#exp_var = os.path.expandvars(path)


#path = "/Users/chenyidan/DFTProject/Wk02_Ex/CodingEnv/Data/data.csv"
#print(path)
columns = ['date', 'value']
df = pd.read_csv(path)
#df = pd.read_csv('/Users/chenyidan/DFTProject/Wk02_Ex/CodingEnv/Data/data.csv', usecols=columns)
plt.plot(df.date, df.value)
#plt.show()
#plt.savefig("/Users/chenyidan/Desktop/data_value.png")
#plt.savefig(os.path.expandvars("$RESEARCH_PATH") + "/Data/data_value.png")
plt.savefig('plot.png', bbox_inches='tight')
