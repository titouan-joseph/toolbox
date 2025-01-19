import pandas as pd
import matplotlib.pyplot as plt
import argparse

# Parser
parser = argparse.ArgumentParser(description='Make graph for TCP-stats')
parser.add_argument('file', type=str, help='csv file with data')
args = parser.parse_args()


df = pd.read_csv(args.file, sep=';')
df.plot(x ='time', y='retransmission_rate', kind='line', title="Retransmission rate", ylabel="Rate (%)", xlabel="Time")
plt.savefig(f'{args.file}_retransmission_rate.png')

ax = df.plot(x ='time', y='ul_kBps', kind='line', colormap='Greens_r', title="Upload and Download speed", ylabel="Speed (KBit/s)", xlabel="Time (s)")
df.plot(x ='time', y='dl_kBps', kind='line', colormap='Reds_r', ax=ax, figsize=(20,5))
plt.savefig(f'{args.file}_dl_ul.png')

plt.show()