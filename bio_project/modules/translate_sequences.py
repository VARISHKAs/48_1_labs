from Bio.Seq import Seq


def translate_rna(rna_sequence):
    
    rna_seq = Seq(rna_sequence)
    protein = rna_seq.translate()
    
    return str(protein)

#Первая функция осуществялет трансляцию без учета старт-кодона; для сравнения результата была написана вторая функция, учитывающая старт-кодон
def translate_rna_with_start_codon(rna_sequence):
    
    rna_seq = Seq(rna_sequence)
    
    # Ищем старт-кодон AUG
    start_pos = rna_sequence.find('AUG')
    
    if start_pos == -1:
        return ""  # Нет старт-кодона
    
    protein = rna_seq[start_pos:].translate()
    
    return str(protein)


