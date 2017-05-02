import numpy as np
import matplotlib
matplotlib.use('tkagg')
matplotlib.rcParams.update({'font.size': 20})
import matplotlib.pyplot as plt

# data to plot
latency = ['0.3ms', '10ms', '50ms']
# create plot

def draw(rpc_call, rpc_cast, latency, filename):
    fig, ax = plt.subplots()
    index = np.arange(len(latency))
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, rpc_call_norm, bar_width,
                     alpha=opacity,
                     color = '#ff3c00',
                     label='RPC call')

    rects2 = plt.bar(index + bar_width, rpc_cast_norm, bar_width,
                     alpha=opacity,
                     color='#ff997a',
                     label='RPC cast')

    plt.xlabel('Latency')
    plt.ylabel('msg/s (normalized)')
    plt.title('Latency impact on RPCs')
    plt.xticks(index + bar_width, latency)
    plt.legend()

#plt.tight_layout()
#plt.show()
    plt.savefig(filename, facecolor='white', transparent=True)

rpc_call = [218., 62., 16.]
mcall = max(rpc_call)
rpc_call_norm = [x/mcall * 100  for x in rpc_call]
rpc_cast = [1062., 84., 18.]
mcast = max(rpc_cast)
rpc_cast_norm = [x/mcast * 100 for x in rpc_cast]

draw(rpc_call_norm, rpc_cast_norm, latency, 'far_client.png')

rpc_call = [215., 37., 14.]
mcall = max(rpc_call)
rpc_call_norm = [x/mcall * 100  for x in rpc_call]
rpc_cast = [1129., 1029., 1170.]
mcast = max(rpc_cast)
rpc_cast_norm = [x/mcast * 100 for x in rpc_cast]

draw(rpc_call_norm, rpc_cast_norm, latency, 'far_server.png')
