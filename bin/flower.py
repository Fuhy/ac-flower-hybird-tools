import itertools

DOMINANCE_MARK = 'RYWS'
RECESSIVE_MARK = 'ryws'
GENE_SEQUENCE = [0, 1, 2, 3]
RED_POS = 0
YELLOW_POS = 1
WHITE_POS = 2
SPECIAL_POS = 3


class Flower:
    def __init__(self, gene):
        self.genotype = gene

    @classmethod
    def constructFromGeneText(cls, geneText):
        # split the str into 4 trunks
        gene_list = []
        chunks = [geneText[i:i + 2] for i in range(0, len(geneText), 2)]
        for eachGene in chunks:
            gene_list.append(
                0b01 if eachGene[0].isupper() ^ eachGene[1].isupper() else eachGene[0].isupper()
            )
        return Flower(gene_list)
        

    def get_genotype(self):
        genotype = []
        for i in GENE_SEQUENCE:
            genotype.append(
                # make it at least has 2 digit
                bin(self.genotype[i])[-2:].replace('b', '0')
                .replace('1', DOMINANCE_MARK[i]).replace('0', RECESSIVE_MARK[i])
            )
        return genotype

    def get_phenotype(self):
        pass

    def generate_gamete(self):
        gametes = [([int(bin(self.genotype[i])[-1])] if self.genotype[i]
                    in (0b00, 0b11) else [0, 1]) for i in GENE_SEQUENCE]
        return list(itertools.product(
            gametes[RED_POS], gametes[YELLOW_POS], gametes[WHITE_POS], gametes[SPECIAL_POS]
        ))


def hybrid(maternal, paternal):
    maternal_gametes = maternal.generate_gamete()
    paternal_gametes = paternal.generate_gamete()
    children = [breed(x, y)
                for x in maternal_gametes for y in paternal_gametes]
    return [Flower(i) for i in children]


def breed(gamete_x, gamete_y):
    child = []
    for i in GENE_SEQUENCE:
        if gamete_x[i] + gamete_y[i] == 2:
            child.append(0b11)
        else:
            child.append(gamete_x[i] + gamete_y[i])
    return child


def pretty_genotype(genotype):
    return ''.join([i[::-1] for i in genotype])
