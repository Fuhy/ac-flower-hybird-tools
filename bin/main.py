import data
import flower

ROSE_DAT = None


def init():
    global ROSE_DAT
    ROSE_DAT = data.acquire_rose_dat()

def predict_child_color_from_color(gene_data, maternal, paternal):
    """Predict the children's color of two flowers. 

    Args:
        gene_data: the data of the mapping from genotype to phenotype.
        maternal, paternal: A color string starts with capital letter like 'Pink'.

    Returns:
        A list of the possible childen's color.
    """
    maternal_gene = get_key_by_value(gene_data, maternal)
    paternal_gene = get_key_by_value(gene_data, paternal)
    print(maternal_gene, paternal_gene)
    color_lists = [predict_rose_child_color_from_gene(
        gene_data, flower.Flower.constrct_from_gene_text(x), flower.Flower.constrct_from_gene_text(y))
        for x in maternal_gene for y in paternal_gene]
    result_set = set()
    for each in color_lists:
        for i in each:
            result_set.add(i)
    return result_set


def predict_child_color_from_gene(gene_data, maternal, paternal):
    """Predict the children's color of two flowers. 

    Args:
        gene_data: the data of the mapping from genotype to phenotype.
        maternal, paternal: A flower instance.
    """
    color = []
    children = flower.hybrid(maternal, paternal)
    children_gene = [i.get_genotype() for i in children]
    for child_gene in set(children_gene):
        color.append(gene_data[child_gene])
    return list(set(color))


def get_key_by_value(dictionary, keyword):
    return [key for key, value in dictionary.items() if value == keyword]
