from data import FLOWER_GENE_DAT
import flower

def predict_child_color_from_color(kind, maternal, paternal):
    """Predict the children's color of two flowers. 

    Args:
        kind: a string in ['Cosmos','Hyacinths','Lilies','Mums','Pansies','Roses','Tulips','Windflowers']
        maternal, paternal: A color string like 'Pink'.

    Returns:
        A list of the possible childen's color.
    """
    maternal = maternal.capitalize()
    paternal = paternal.capitalize()
    gene_data = get_gene_mapping(kind)
    maternal_gene = get_key_by_value(gene_data, maternal)
    paternal_gene = get_key_by_value(gene_data, paternal)
    color_lists = [predict_child_color_from_gene(
        kind, flower.Flower.constrct_from_gene_text(kind,x), flower.Flower.constrct_from_gene_text(kind,y))
        for x in maternal_gene for y in paternal_gene]
    result_set = set()
    for each in color_lists:
        for i in each:
            result_set.add(i)
    return result_set


def predict_child_color_from_gene(kind, maternal, paternal):
    """Predict the children's color of two flowers. 

    Args:
        kind: a string in ['Cosmos','Hyacinths','Lilies','Mums','Pansies','Roses','Tulips','Windflowers']
        maternal, paternal: A flower instance.

    Returns:
        A list of the possible childen's color.
    """
    color = []
    children = flower.hybrid(maternal, paternal)
    children_gene = [i.get_genotype() for i in children]
    for child_gene in set(children_gene):
        color.append(get_gene_mapping(kind)[child_gene])
    return list(set(color))


def predict_child_color_from_color_with_restrain(kind, maternal, paternal, restrain):
    """Predict the children's color of two flowers. Filter possible with restrain.

    To make the result more specific, you need to provide more infomation like the previous hybrid result.
    By giving a list of previous hybrid result, we can make the result set smaller.

    Args:
        kind: a string in ['Cosmos','Hyacinths','Lilies','Mums','Pansies','Roses','Tulips','Windflowers']
        maternal, paternal: A color string starts with capital letter like 'Pink'.
        restrain: A list of color string, which presents the previous hybrid result.

    Returns:
        A list of the possible childen's color.
    """
    maternal = maternal.capitalize()
    paternal = paternal.capitalize()
    restrain = [color.capitalize() for color in restrain]
    gene_data = get_gene_mapping(kind)
    maternal_gene = get_key_by_value(gene_data, maternal)
    paternal_gene = get_key_by_value(gene_data, paternal)
    result_set = set()
    for x in maternal_gene:
        for y in paternal_gene:
            flowerx = flower.Flower.constrct_from_gene_text(kind, x)
            flowery = flower.Flower.constrct_from_gene_text(kind, y)
            child_color_set = set(predict_child_color_from_gene(kind, flowerx, flowery))
            print(child_color_set)
            if set(restrain) <= child_color_set:
                result_set |= child_color_set
    return result_set

def get_gene_mapping(kind):
    """Get the data which is the mapping from genotype to phenotype

    Args:
        kind: a string in ['Cosmos','Hyacinths','Lilies','Mums','Pansies','Roses','Tulips','Windflowers']
    
    Returns:
        A dictionary of mapping data.
    """
    return FLOWER_GENE_DAT[flower.FLOWER_KIND[kind.capitalize()]]


def get_key_by_value(dictionary, keyword):
    return [key for key, value in dictionary.items() if value == keyword]
