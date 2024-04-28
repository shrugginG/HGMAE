import numpy as np

####################################################
# This tool is to collect neighbors, and reform them
# as numpy.array style for futher usage.
####################################################

# This is for phishing
fu = np.genfromtxt("/home/jxlu/project/HGMAE/data/phishing/fu.txt")

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
np.save("/home/jxlu/project/HGMAE/data/phishing/nei_f.npy", u_n)

# give some basic statistics about neighbors
l = [len(i) for i in u_n]
print(max(l), min(l), np.mean(l))

# # This is for ACM, Freebase, AMiner
# pa = np.genfromtxt("./aminer/pa.txt")
# p_n = {}
# for i in pa:
#     if i[0] not in p_n:
#         p_n[int(i[0])] = []
#         p_n[int(i[0])].append(int(i[1]))
#     else:
#         p_n[int(i[0])].append(int(i[1]))

# keys = sorted(p_n.keys())
# p_n = [p_n[i] for i in keys]
# p_n = np.array([np.array(i) for i in p_n])
# np.save("nei_a.npy", p_n)

# # give some basic statistics about neighbors
# l = [len(i) for i in p_n]
# print(max(l), min(l), np.mean(l))
