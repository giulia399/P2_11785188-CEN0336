import sys
from Bio import SeqIO
from Bio.Seq import Seq

def encontrar_orfs_em_frame(seq, frame):
    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}
    orfs = []
    comprimento = len(seq)

    for i in range(frame, comprimento - 2, 3):
        codon = seq[i:i+3]
        if codon == start_codon:
            for j in range(i + 3, comprimento - 2, 3):
                stop_codon = seq[j:j+3]
                if stop_codon in stop_codons:
                    if (j + 3 - i) % 3 == 0:
                        orfs.append((seq[i:j+3], frame + 1, i + 1, j + 3))  # Salva sequência e coordenadas
                        break
    return orfs

def maior_orf(seq):
    seq_obj = Seq(seq)
    frames = [
        str(seq_obj),
        str(seq_obj[1:]),
        str(seq_obj[2:]),
        str(seq_obj.reverse_complement()),
        str(seq_obj.reverse_complement()[1:]),
        str(seq_obj.reverse_complement()[2:])
    ]

    maior_orf = ("", 0, 0, 0)  # Inicialmente vazio
    for i, frame in enumerate(frames):
        orfs = encontrar_orfs_em_frame(frame, 0)
        if orfs:
            orf_mais_longo = max(orfs, key=lambda x: len(x[0]))  # Encontra o maior ORF
            if len(orf_mais_longo[0]) > len(maior_orf[0]):
                maior_orf = (orf_mais_longo[0], i + 1, orf_mais_longo[2], orf_mais_longo[3])

    return maior_orf

def processar_multifasta(arquivo_fasta, saida_fasta_dna, saida_fasta_peptideos):
    with open(arquivo_fasta, "r") as entrada, \
         open(saida_fasta_dna, "w") as saida_dna, \
         open(saida_fasta_peptideos, "w") as saida_peptideos:
        
        for registro in SeqIO.parse(entrada, "fasta"):
            maior_orf_seq, frame, start, end = maior_orf(str(registro.seq))
            if maior_orf_seq:
                # Formata o identificador com coordenadas e frame
                identificador = f"{registro.id}_frame{frame}_{start}_{end}"
                
                # Salva o maior ORF no arquivo .fna
                saida_dna.write(f">{identificador}\n{maior_orf_seq}\n")
                
                # Tradução do maior ORF para peptídeo
                peptideo = str(Seq(maior_orf_seq).translate(to_stop=True))
                
                # Salva o peptídeo no arquivo .faa
                saida_peptideos.write(f">{identificador}\n{peptideo}\n")
            else:
                # Caso não haja ORFs, ainda salvamos a entrada
                identificador = f"{registro.id}_Nenhum_ORF"
                saida_dna.write(f">{identificador}\nNenhum_ORF_encontrado\n")
                saida_peptideos.write(f">{identificador}\nNenhum_peptídeo\n")

# Verifica os argumentos de linha de comando
if len(sys.argv) != 2:
    print("Uso: python script_getORF.py <arquivo_multifasta>")
    sys.exit(1)

# Captura o nome do arquivo multifasta
arquivo_multifasta = sys.argv[1]

# Nomes dos arquivos de saída
saida_fasta_dna = "ORF.fna"
saida_fasta_peptideos = "ORF.faa"

# Processa o arquivo multifasta
processar_multifasta(arquivo_multifasta, saida_fasta_dna, saida_fasta_peptideos)




