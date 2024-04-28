import pandas as pd
import numpy as np


def trans_labels(data_dir, export_dir):

    with open(f"{data_dir}/url_nodes.csv") as f:
        url_nodes = pd.read_csv(f)

    node_labels = []

    for row in url_nodes.iterrows():
        if row[1]["category"] == "benign":
            node_labels.append(0)
        elif row[1]["category"] == "phishy":
            node_labels.append(1)

    label_array = np.array(node_labels, dtype="int32")

    label_npy_file = f"{export_dir}/labels.npy"

    np.save(label_npy_file, label_array)


def generate_nei_f(data_dir, export_dir):
    nei_f = [[] for _ in range(1018)]
    with open(f"{data_dir}/url_fqdn_relation_edges.csv") as f:
        url_fqdn_relation_edges = pd.read_csv(f)

    url_fqdn_relation_edges["url_id"] = url_fqdn_relation_edges["url_id"] - 1
    url_fqdn_relation_edges["fqdn_id"] = url_fqdn_relation_edges["fqdn_id"] - 1

    for row in url_fqdn_relation_edges.iterrows():
        if row[1]["fqdn_id"] not in nei_f[row[1]["url_id"]]:
            nei_f[row[1]["url_id"]].append(row[1]["fqdn_id"])
        # else:
        #     print("false")

    nei_f = [np.array(nei) for nei in nei_f]

    object_array = np.array(nei_f, dtype="object")

    npy_file = f"{export_dir}/nei_f.npy"

    np.save(npy_file, object_array)


# def export_url_fqdn_edge_to_txt(data_dir, export_dir):
#     with open(f"{data_dir}/url_fqdn_relation_edges.csv") as f:
#         url_fqdn_relation_edges = pd.read_csv(f)

#     url_fqdn_relation_edges["url_id"] = url_fqdn_relation_edges["url_id"] - 1
#     url_fqdn_relation_edges["fqdn_id"] = url_fqdn_relation_edges["fqdn_id"] - 1

#     txt_lines = []
#     for row in url_fqdn_relation_edges.iterrows():
#         txt_lines.append([row[1]["fqdn_id"], row[1]["url_id"]])

#     txt_lines.sort()
#     txt_lines = [f"{txt_line[0]}\t{txt_line[1]}\n" for txt_line in txt_lines]
#     with open(f"{export_dir}/fu.txt", "w") as f:
#         f.writelines(txt_lines)


# def export_fqdn_registered_domain_edge_to_txt(data_dir, export_dir):
#     with open(f"{data_dir}/fqdn_registered_domain_relation_edges.csv") as f:
#         fqdn_registered_domain_relation_edges = pd.read_csv(f)

#     fqdn_registered_domain_relation_edges["fqdn_id"] = (
#         fqdn_registered_domain_relation_edges["fqdn_id"] - 1
#     )
#     fqdn_registered_domain_relation_edges["registered_domain_id"] = (
#         fqdn_registered_domain_relation_edges["registered_domain_id"] - 1
#     )

#     txt_lines = []
#     for row in fqdn_registered_domain_relation_edges.iterrows():
#         txt_lines.append([row[1]["fqdn_id"], row[1]["registered_domain_id"]])

#     txt_lines.sort()
#     txt_lines = [f"{txt_line[0]}\t{txt_line[1]}\n" for txt_line in txt_lines]
#     with open(f"{export_dir}/fr.txt", "w") as f:
#         f.writelines(txt_lines)

def export_fqdn_ip_edge_to_txt(data_dir, export_dir):
    with open(f"{data_dir}/fqdn_ip_relation_edges.csv") as f:
        fqdn_ip_relation_edges = pd.read_csv(f)

    fqdn_ip_relation_edges["fqdn_id"] = (
        fqdn_ip_relation_edges["fqdn_id"] - 1
    )
    fqdn_ip_relation_edges["ip_id"] = (
        fqdn_ip_relation_edges["ip_id"] - 1
    )

    txt_lines = []
    for row in fqdn_ip_relation_edges.iterrows():
        txt_lines.append([row[1]["fqdn_id"], row[1]["ip_id"]])

    txt_lines.sort()
    txt_lines = [f"{txt_line[0]}\t{txt_line[1]}\n" for txt_line in txt_lines]
    with open(f"{export_dir}/fi.txt", "w") as f:
        f.writelines(txt_lines)

if __name__ == "__main__":

    data_dir = "/home/jxlu/project/HGMAE/data/neo4j_mysql_export"
    export_dir = "/home/jxlu/project/HGMAE/data/phishing"
    # trans_labels(data_dir, export_dir)

    # generate_nei_f(data_dir, export_dir)

    export_fqdn_ip_edge_to_txt(data_dir, export_dir)
