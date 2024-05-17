import numpy as np
import scipy.sparse as sp
import pandas as pd

####################################################
# This tool is to generate meta-path based adjacency
# matrix given original links.
####################################################

data_dir = "/home/jxlu/project/HGMAE/data/neo4j_mysql_export_1000"
export_dir = "/home/jxlu/project/HGMAE/data/phishing_1000"

fu = np.genfromtxt(f"{export_dir}/fu.txt")
fr = np.genfromtxt(f"{export_dir}/fr.txt")
fi = np.genfromtxt(f"{export_dir}/fi.txt")

# pa = np.genfromtxt("./dblp/pa.txt")
# pc = np.genfromtxt("./dblp/pc.txt")
# pt = np.genfromtxt("./dblp/pt.txt")

# U = 1018
# F = 5164
# R = 1910
# I = 6172

with open(f"{data_dir}/url_nodes.csv") as f:
    url_nodes = pd.read_csv(f)
    U = url_nodes.iloc[-1]["url_id"]

with open(f"{data_dir}/fqdn_nodes.csv") as f:
    fqdn_nodes = pd.read_csv(f)
    F = fqdn_nodes.iloc[-1]["fqdn_id"]

with open(f"{data_dir}/registered_domain_nodes.csv") as f:
    registered_domain_nodes = pd.read_csv(f)
    R = registered_domain_nodes.iloc[-1]["registered_domain_id"]

with open(f"{data_dir}/ip_nodes.csv") as f:
    ip_nodes = pd.read_csv(f)
    I = ip_nodes.iloc[-1]["ip_id"]

print(U, F, R, I)

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
sp.save_npz(f"{export_dir}/ufu.npz", ufu)

ufr = np.matmul(fu_.T, fr_) > 0
ufrfu = np.matmul(ufr, ufr.T) > 0
ufrfu = sp.coo_matrix(ufrfu)
sp.save_npz(f"{export_dir}/ufrfu.npz", ufrfu)

ufi = np.matmul(fu_.T, fi_) > 0
ufifu = np.matmul(ufi, ufi.T) > 0
ufifu = sp.coo_matrix(ufifu)
sp.save_npz(f"{export_dir}/ufifu.npz", ufifu)

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
