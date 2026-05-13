
from modules.fetch_sequences import read_fasta_from_input, read_fasta_from_file, save_results
from modules.analyze_gc import find_highest_gc
from modules.translate_sequences import translate_rna, translate_rna_with_start_codon


def main():
    print("=" * 50)
    print("ЛАБОРАТОРНАЯ РАБОТА №2")
    print("=" * 50)
    
    print("\nВыберите вариант:")
    print("1 - Анализ GC-состава (Вариант 1)")
    print("2 - Трансляция РНК (Вариант 2)")
    
    choice = input("\nВаш выбор (1 или 2): ").strip()
    
    if choice == "1":
        run_gc_analysis()
    elif choice == "2":
        run_translation()
    else:
        print("Неверный выбор!")


def run_gc_analysis():
   
    print("\n" + "=" * 50)
    print("АНАЛИЗ GC-СОСТАВА")
    print("=" * 50)
    
    print("\nКак вы хотите ввести данные?")
    print("1 - Ручной ввод")
    print("2 - Загрузка из файла")
    
    input_method = input("Ваш выбор: ").strip()
    
    if input_method == "1":
        sequences = read_fasta_from_input()
    else:
        filename = input("Введите имя файла: ")
        sequences = read_fasta_from_file(filename)
    
    if not sequences:
        print("Нет последовательностей для анализа!")
        return
    
    # Находим последовательность с максимальным GC
    best_id, best_gc = find_highest_gc(sequences)
    
    
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТ:")
    print(best_id)
    print(f"{best_gc:.6f}")
    
  
    result_text = f"{best_id}\n{best_gc:.6f}"
    save_results(result_text, "gc_result.txt")
    print("\nРезультат сохранен в output/gc_result.txt")
    

def run_translation():

    print("\n" + "=" * 50)
    print("ТРАНСЛЯЦИЯ РНК")
    print("=" * 50)
    
    print("\nКак вы хотите ввести данные?")
    print("1 - ручной ввод")
    print("2 - Загрузика из FASTA файла")
    
    input_method = input("Ваш выбор: ").strip()
    
    if input_method == "1":
        print("\nВведите последовательность РНК (не более 10000 символов):")
        rna_sequence = input().strip()
        
        if len(rna_sequence) > 10000:
            print("Ошибка: длина последовательности превышает 10000 символов!")
            return
        
        print("\nТрансляция (без учета старт-кодона):")
        protein = translate_rna(rna_sequence)
        print(protein)
        
        print("\nТрансляция (с учетом старт-кодона):")
        protein_with_start = translate_rna_with_start_codon(rna_sequence)
        print(protein_with_start)
        
        # Сохраняем результат
        result_text = f"РНК: {rna_sequence}\n\nБелок (без старт-кодона):\n{protein}\n\nБелок (со старт-кодоном):\n{protein_with_start}"
        save_results(result_text, "translation_result.txt")
        print("\nРезультат сохранен в output/translation_result.txt")
        
    else:
        filename = input("Введите имя FASTA файла: ")
        sequences = read_fasta_from_file(filename)
        
        for record in sequences:
            rna_sequence = str(record.seq)
            protein = translate_rna(rna_sequence)
            print(f"\n>{record.id}")
            print(protein)


if __name__ == "__main__":
    main()
