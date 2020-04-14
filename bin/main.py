import data
import flower

ROSE_DAT = None

def init():
    global ROSE_DAT 
    ROSE_DAT = data.acquire_rose_dat()


def predict_rose_child_color(maternal, paternal):
    color = []
    children = flower.hybrid(maternal,paternal)
    children_gene = [ flower.pretty_genotype(i.get_genotype()) for i in children]
    for child_gene in set(children_gene):
        color.append(ROSE_DAT[child_gene])
    return set(color)

