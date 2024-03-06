def total_salary(path):
    total = 0
    count = 0
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            name, salary = line.strip().split(',')
            count += 1
            total += int(salary)
        average = int(total/count) if count > 0 else 0
        
    return total, average
    

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")