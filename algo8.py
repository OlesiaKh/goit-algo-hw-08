import heapq
def min_cost_to_connect_cables(cable_lengths):
    if not cable_lengths:
        return 0
    
    # Ініціалізація мінімальної купи
    heapq.heapify(cable_lengths)
    total_cost = 0

    # Об'єднання кабелів, поки в купі більше одного кабеля
    while len(cable_lengths) > 1:

        # Витягуємо два найменших кабелі
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        # Об'єднуємо кабелі та додаємо вартість об'єднання до загальних витрат
        cost = first + second
        total_cost += cost
        
        # Додаємо новий об'єднаний кабель до купи
        heapq.heappush(cable_lengths, cost)
    return total_cost

if __name__ == '__main__':
    # Приклад використання
    cable_lengths = [4, 6, 8, 12]
    print("Мінімальні витрати на об'єднання кабелів:", min_cost_to_connect_cables(cable_lengths))
