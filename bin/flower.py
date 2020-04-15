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
        """Construct Flower instance from gene sequence.

        Args:
            gene: A gene sequence is a list like [0b01,0b11,0b00,0b00], which present the gene text 'RrYYwwsss'.

        Returns:
            An instance of Flower.
        """
        self.genotype = gene

    @classmethod
    def constrct_from_gene_text(cls, gene_text):
        """Construct Flower instance from Gene Text.

        Gene Text is a string like 'RrYyWwSS'. This method will decode the text into
        binary sequence then store into variable genotype. For example, 'Rr' will be store as 0b01.

        Args: 
            gene_text: A string has a pattern like [Rr]{2}[Yy]{2}[Ww]{2}[Ss]{2} .

        Returns:
            An instance of Flower.
        """
        # split the str into 4 trunks
        gene_list = []
        chunks = [gene_text[i:i + 2] for i in range(0, len(gene_text), 2)]
        for eachGene in chunks:
            gene_list.append(
                0b01 if eachGene[0].isupper() ^ eachGene[1].isupper() else (0b11 if eachGene[0].isupper() else 0b00)
            )
        return Flower(gene_list)
        

    def get_genotype(self):
        """Return the gene text of the flower.

        Returns:
            The gene text like 'RrYYWWSS'.
        """
        genotype = []
        for i in GENE_SEQUENCE:
            genotype.append(
                # make it at least has 2 digit
                bin(self.genotype[i])[-2:].replace('b', '0')
                .replace('1', DOMINANCE_MARK[i]).replace('0', RECESSIVE_MARK[i])
            )
        # make upper letters in the first bit in a chunk
        return ''.join([i[::-1] for i in genotype])

    def generate_gamete(self):
        """Generate the possible gametes of a flower.

        A gamete's gene sequence is a tuple like (0,0,1,1), which presents 'r,y,W,S'.

        Returns:
            A tuple list of gametes' gene sequence like [(0,0,1,1)].
        """
        gametes = [([int(bin(self.genotype[i])[-1])] if self.genotype[i]
                    in (0b00, 0b11) else [0, 1]) for i in GENE_SEQUENCE]
        return list(itertools.product(
            gametes[RED_POS], gametes[YELLOW_POS], gametes[WHITE_POS], gametes[SPECIAL_POS]
        ))



def hybrid(maternal, paternal):
    """Hybrid two flowers and get the possible children.

    Args:
        maternal, paternal: the two flower you want to hybrid.

    Returns:
        the pssible children as flower instances.
    """
    maternal_gametes = maternal.generate_gamete()
    paternal_gametes = paternal.generate_gamete()
    children = [breed(x, y)
                for x in maternal_gametes for y in paternal_gametes]
    return [Flower(i) for i in children]


def breed(gamete_x, gamete_y):
    """Breed the gametes.

    Args: 
        gamete, aka gene sequence.

    Returns:
        child's gene sequence.
    """
    child = []
    for i in GENE_SEQUENCE:
        if gamete_x[i] + gamete_y[i] == 2:
            child.append(0b11)
        else:
            child.append(gamete_x[i] + gamete_y[i])
    return child


def parse_phenotype(self, gene_data):
    """Parse a flower's color.

    Since the identical gene text can present different color in different kinds of flower,
    you need to provide the mapping data.

    Args:
        gene_data: the data of the mapping from genotype to phenotype.
    """
