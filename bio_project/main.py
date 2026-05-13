
import sys 
from modules.fetch_sequences import read_fasta_from_input, save_result
from modules.analyze_gc import find_highest_gc
from modules.translate_sequences import translate_rna, translate_rna_with_start_codon


def main():
    print("=" * 50)
    print("ЛАБОРАТОРНЫЕ РАБОТЫ ПО БИОИНФОРМАТИКЕ")
    print("=" * 50)
    
    print("\nВыберите лабораторную работу:")
    print("1 - Лабораторная работа №2 (Вариант 1: GC-состав)")
    print("2 - Лабораторная работа №2 (Вариант 2: Трансляция РНК)")
    print("3 - Лабораторная работа №3 (Вариант 1: Iris диаграмма)")
    print("4 - Лабораторная работа №3 (Вариант 2: CO2 динамика)")
    print("0 - Выход")
    
    choice = input("\nВаш выбор: ").strip()
    
    if choice == "1":
        run_variant1_lab2()
    elif choice == "2":
        run_variant2_lab2()
    elif choice == "3":
        run_lab3_v1()
    elif choice == "4":
        run_lab3_v2()
    elif choice == "0":
        print("До свидания!")
        sys.exit() 
    else:
        print("Неверный выбор!")


def run_variant1_lab2():
  
    print("\n" + "=" * 50)
    print("ВАРИАНТ 1. ВЫЧИСЛЕНИЕ GC-СОСТАВА")
    print("=" * 50)
    
    sequences = read_fasta_from_input()
    
    if not sequences:
        print("Нет последовательностей для анализа!")
        return
    
    best_id, best_gc = find_highest_gc(sequences)
    
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТ:")
    print(best_id)
    print(f"{best_gc:.6f}")
    
    save_result(f"{best_id}\n{best_gc:.6f}", "gc_result.txt")
    print("\nРезультат сохранен в output/gc_result.txt")


def run_variant2_lab2():
   
    print("\n" + "=" * 50)
    print("ВАРИАНТ 2. ТРАНСЛЯЦИЯ РНК")
    print("=" * 50)
    
    print("\nВведите последовательность РНК (не более 10000 символов):")
    rna_sequence = input().strip()
    
    if len(rna_sequence) > 10000:
        print("Ошибка: длина последовательности превышает 10000 символов!")
        return
    
    print("\n" + "=" * 50)
    print("Трансляция (без учета старт-кодона):")
    protein = translate_rna(rna_sequence)
    print(protein)
    
    print("\n" + "=" * 50)
    print("Трансляция (с учетом старт-кодона):")
    protein_with_start = translate_rna_with_start_codon(rna_sequence)
    print(protein_with_start)
    
    result_text = f"РНК: {rna_sequence}\n\nБелок (без старт-кодона):\n{protein}\n\nБелок (со старт-кодоном):\n{protein_with_start}"
    save_result(result_text, "translation_result.txt")
    print("\nРезультат сохранен в output/translation_result.txt")


def run_lab3_v1():
    
    print("\n" + "=" * 50)
    print("ЛАБОРАТОРНАЯ РАБОТА №3 (Вариант 1)")
    print("Диаграмма рассеяния для ирисов Фишера")
    print("=" * 50)
    print("\nЗапуск программы...")
    
    exec(open("lab_3_v1.py").read())


def run_lab3_v2():
    
    print("\n" + "=" * 50)
    print("ЛАБОРАТОРНАЯ РАБОТА №3 (Вариант 2)")
    print("Динамика концентрации CO2 в атмосфере")
    print("=" * 50)
    print("\nЗапуск программы...")
    
    exec(open("lab_3_v2.py").read())


if __name__ == "__main__":
    main()
