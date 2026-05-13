def calculate_gc_content(sequence):
    
    if len(sequence) == 0:
        return 0.0
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

def find_highest_gc(sequences):
    
    max_gc_id = ""
    max_gc_value = 0.0
    
   
    for record in sequences:
        sequence = str(record.seq).upper()
        
        if len(sequence) > 1000:
            print(f"Предупреждение: Последовательность {record.id} имеет длину {len(sequence)} нуклеотидов, что превышает лимит в 1000 нуклеотидов. Она будет пропущена.")
            continue
        
        gc_content = calculate_gc_content(sequence)
        
        if gc_content > max_gc_value:
            max_gc_value = gc_content
            max_gc_id = record.id
    
    return max_gc_id, max_gc_value



