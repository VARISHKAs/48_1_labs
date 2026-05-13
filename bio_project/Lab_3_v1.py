import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

iris_data = load_iris()

df = pd.DataFrame(
    data=iris_data.data,  
    columns=iris_data.feature_names)

# В 'target' хранятся числа: 0, 1, 2 - соответствуют своему виду
df['target'] = iris_data.target


# В 'target_names' хранятся: ['setosa' 'versicolor' 'virginica']
df['species'] = df['target'].map({
    0: iris_data.target_names[0],  # setosa
    1: iris_data.target_names[1],  # versicolor
    2: iris_data.target_names[2]   # virginica
})

# выведем первые 5 строк
print("Первые 5 строк данных:")
print(df.head())

# Строим диаграмму рассеяния
# Создаем окно с графиком размером 10x6 дюймов
plt.figure(figsize=(10, 6))

# Получаем уникальные виды и цвета для них
species_list = df['species'].unique()  # ['setosa', 'versicolor', 'virginica']
colors = ['red', 'blue', 'green']

# Рисуем точки для каждого вида отдельно (чтобы была легенда)
for species, color in zip(species_list, colors):
    # Выбираем только строки с текущим видом
    mask = df['species'] == species #(логический массив, который содержит True для строк, удовлетворяющих условию, и False для всех остальных.)
    
    # Рисуем точки: X = sepal length, Y = sepal width
    #loc[] - это метод для доступа к данным по меткам (индексам). 
    #Когда мы передаем маску, он выбирает только те строки, где маска = True.
    #plt.scatter - диаграмма рассеяния 
    plt.scatter(
        x=df.loc[mask, 'sepal length (cm)'],  # данные по оси X
        y=df.loc[mask, 'sepal width (cm)'],   # данные по оси Y
        c=color,                               # цвет точек
        label=species,                          # название для легенды
        alpha=0.7,                               # небольшая прозрачность, чтобы наложения было видно)
        s=50                                      # размер точек
    )

# Добавляем заголовок и подписи осей
plt.title('Диаграмма рассеяния для ирисов Фишера', fontsize=16)
plt.xlabel('Длина чашелистика (sepal length, cm)', fontsize=12)
plt.ylabel('Ширина чашелистика (sepal width, cm)', fontsize=12)

# Добавляем легенду и сетку
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)  # сетка с прозрачностью 30%

# Показываем график
plt.tight_layout()  # подгоняем элементы, чтобы не обрезались
plt.show()

# Дополнительно: посчитаем базовую статистику
print("\nБазовая статистика по каждому виду:")
print(df.groupby('species')[['sepal length (cm)', 'sepal width (cm)']].describe())