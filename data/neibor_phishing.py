import numpy as np

####################################################
# This tool is to collect neighbors, and reform them
# as numpy.array style for futher usage.
####################################################


# def get_nei(data_dir, target):
#     relation = np.genfromtxt(f"{data_dir}/{target}.txt")
#     nodes_neigh = {}
#     for edge in relation:
#         if int(edge[0]) not in nodes_neigh:
#             nodes_neigh[int(edge[0])] = []
#             nodes_neigh[int(edge[0])].append(int(edge[1]))
#         else:
#             nodes_neigh[int(edge[0])].append(int(edge[1]))

#     keys = sorted(nodes_neigh.keys())

#     nodes_neigh = [nodes_neigh[i] for i in keys]
#     nodes_neigh = [np.array(nei) for nei in nodes_neigh]
#     # print(nodes_neigh)
#     print(type(nodes_neigh[0]))
#     nodes_neigh = np.array(nodes_neigh, dtype=object)
#     print(nodes_neigh)
#     np.save(f"{data_dir}/nei_{target}.npy", nodes_neigh)
    
#     return nodes_neigh


# This is for phishing_1000
fu = np.genfromtxt("/home/jxlu/project/HGMAE/data/phishing_1000/fu.txt")
print(len(fu))
u_n = {}
for i in fu:
    if i[1] not in u_n:
        u_n[int(i[1])] = []
        u_n[int(i[1])].append(int(i[0]))
    else:
        u_n[int(i[1])].append(int(i[0]))
keys = sorted(u_n.keys())
u_n = [u_n[i] for i in keys]
u_n = [np.array(nei) for nei in u_n]
u_n = np.array(u_n, dtype="object")
np.save("/home/jxlu/project/HGMAE/data/phishing_1000/nei_f.npy", u_n)

# give some basic statistics about neighbors
l = [len(i) for i in u_n]
print(max(l), min(l), np.mean(l))

# if __name__ == "__main__":
#     data_dir = "/home/jxlu/project/HGMAE/data/phishing"
#     targets = ["fu", "fr"]
#     for target in targets:
#         nei = get_nei(data_dir, target)
#         l = [len(i) for i in nei]
#         print(max(l), min(l), np.mean(l))
