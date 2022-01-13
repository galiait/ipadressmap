import pandas as pd
import networkx as nx
from loc import map_network
from pyvis.network import Network

def network_maping(base):
    """Function for mapping and visualization of devices on network.

    Parameters
    ----------
    base : list
        List of IP adresses of devices on network.

    """
    
    lis = map_network() # list of devices that were mapped
    
    def check_on(l1, l2): # function to assign color to item, i.e. the IP adress, to determine wheter it is active or not
        c = list()
        for item in l1:
            if item in l2:
                c.append('green')
            else:
                c.append('red')
        return c

    col = check_on(base, lis[1:]) 

    # initialize the network graph
    got_net = Network(height = '750px', 
                      width = '100%', 
                      bgcolor = '#222222', 
                      font_color = 'white'
                      )
    
    sources = base # base IP adresses are sources on map
    targets = [lis[0]]*len(base) # targets are mapped IP adresses
    color = col

    edge_data = zip(sources, targets, color)

    for src, dst, cl in edge_data:
        #add nodes and edges to the graph
        got_net.add_node(src, 
                         src, 
                         title = src, 
                         color = cl
                         )
        got_net.add_node(dst, 
                         dst, 
                         title = dst, 
                         color = cl
                         )

        got_net.add_edge(src, 
                         dst
                         )

    neighbor_map = got_net.get_adj_list()

    # add neighbor data to node hover data
    for node in got_net.nodes:
        node['title'] += ' Neighbors:<br>' + '<br>'.join(neighbor_map[node['id']])
        node['value'] = len(neighbor_map[node['id']])

    got_net.show('loc_ip.html')