from Bio import SeqIO

def read_fasta_from_file(filename):
    
    sequences = []
    for record in SeqIO.parse(filename, "fasta"):
        sequences.append(record)
    return sequences

def read_fasta_from_input():

    print("Введите последовательности в формате FASTA:")
    print("   - Каждую последовательность вводите отдельно. При едином вводе, каждая последовательность должна содержать идентификатор ")
    print("(Для завершения ввода введите пустую строку)")
    
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    
    # Сохраняем в временный файл
    temp_file = "temp_input.fasta"
    with open(temp_file, "w") as f:
        for line in lines:
            f.write(line + "\n")
    
    # Читаем временный файл
    sequences = read_fasta_from_file(temp_file)
    return sequences

def save_results(content, filename):
    
    with open(f"output/{filename}", "w") as f:
        f.write(content)