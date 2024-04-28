import numpy as np
import scipy.sparse as sp

####################################################
# This tool is to generate meta-path based adjacency
# matrix given original links.
####################################################

fu = np.genfromtxt("/home/jxlu/project/HGMAE/data/phishing/fu.txt")
fr = np.genfromtxt("/home/jxlu/project/HGMAE/data/phishing/fr.txt")
fi = np.genfromtxt("/home/jxlu/project/HGMAE/data/phishing/fi.txt")

# pa = np.genfromtxt("./dblp/pa.txt")
# pc = np.genfromtxt("./dblp/pc.txt")
# pt = np.genfromtxt("./dblp/pt.txt")

U = 1018
F = 5164
R = 1910
I = 6172

# A = 4057
# P = 14328
# C = 20
# T = 7723

fu_ = sp.coo_matrix(
    (np.ones(fu.shape[0]), (fu[:, 0], fu[:, 1])), shape=(F, U)
).toarray()
fr_ = sp.coo_matrix(
    (np.ones(fr.shape[0]), (fr[:, 0], fr[:, 1])), shape=(F, R)
).toarray()
fi_ = sp.coo_matrix(
    (np.ones(fi.shape[0]), (fi[:, 0], fi[:, 1])), shape=(F, I)
).toarray()

ufu = np.matmul(fu_.T, fu_) > 0
ufu = sp.coo_matrix(ufu)
sp.save_npz("/home/jxlu/project/HGMAE/data/phishing/ufu.npz", ufu)

ufr = np.matmul(fu_.T, fr_) > 0
ufrfu = np.matmul(ufr, ufr.T) > 0
ufrfu = sp.coo_matrix(ufrfu)
sp.save_npz("/home/jxlu/project/HGMAE/data/phishing/ufrfu.npz", ufrfu)

ufi = np.matmul(fu_.T, fi_) > 0
ufifu = np.matmul(ufi, ufi.T) > 0
ufifu = sp.coo_matrix(ufifu)
sp.save_npz("/home/jxlu/project/HGMAE/data/phishing/ufifu.npz", ufifu)

# apa = np.matmul(pa_.T, pa_) > 0
# apa = sp.coo_matrix(apa)
# sp.save_npz("./dblp/apa.npz", apa)

# apc = np.matmul(pa_.T, pc_) > 0
# apcpa = np.matmul(apc, apc.T) > 0
# apcpa = sp.coo_matrix(apcpa)
# sp.save_npz("./dblp/apcpa.npz", apcpa)

# apt = np.matmul(pa_.T, pt_) > 0
# aptpa = np.matmul(apt, apt.T) > 0
# aptpa = sp.coo_matrix(aptpa)
# sp.save_npz("./dblp/aptpa.npz", aptpa)
