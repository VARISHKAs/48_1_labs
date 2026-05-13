
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm  


co2_data = sm.datasets.co2.load_pandas()
co2_series = co2_data.data


# ШАГ 2: Преобразуем в DataFrame для удобства фильтрации
# Сбрасываем индекс, чтобы дата стала отдельным столбцом

#reset_index() - превращает даты из индекса в обычный столбец
df_co2 = co2_series.reset_index()
df_co2.columns = ['date', 'co2_concentration']  # переименовываем столбцы



# Создаем маску (условие) для фильтрации
mask = (df_co2['date'] >= '1958-01-01') & (df_co2['date'] <= '1980-12-31')
df_filtered = df_co2[mask].copy()  # .copy() чтобы не было предупреждений

# обработка пропущенных знаений 
missing_values = df_filtered['co2_concentration'].isna().sum()
print(f"Пропущенных значений: {missing_values}")

# Если есть пропуски, заполним их способом интерполяции
if missing_values > 0:
    df_filtered['co2_concentration'] = df_filtered['co2_concentration'].interpolate()
    

# Создаем фигуру размером 12x6 дюймов
plt.figure(figsize=(12, 6))

# Строим линейный график
plt.plot(
    df_filtered['date'],           # даты по оси X
    df_filtered['co2_concentration'],  # концентрация CO2 по оси Y
    color='red',                    # цвет линии
    linewidth=2,                    # толщина линии
    markersize=3,                    # размер маркеров
    markerfacecolor='blue',          # цвет заливки маркеров
    markeredgecolor='darkblue',      # цвет границы маркеров
    label='CO2 концентрация'         # название для легенды
)

# Добавляем заголовок и подписи осей
plt.title('Динамика концентрации CO2 в атмосфере (1958-1980)', fontsize=16)
plt.xlabel('Год', fontsize=12)
plt.ylabel('Концентрация CO2 (ppm)', fontsize=12)

# Настраиваем сетку
plt.grid(True, alpha=0.3, linestyle='--')

# Поворачиваем подписи дат для лучшей читаемости
plt.xticks(rotation=45)

# Добавляем легенду
plt.legend(fontsize=10)

# Добавляем горизонтальную линию среднего значения для наглядности
mean_co2 = df_filtered['co2_concentration'].mean()
plt.axhline(y=mean_co2, color='gray', linestyle=':', alpha=0.7, 
            label=f'Среднее: {mean_co2:.1f} ppm')

# Обновляем легенду с учетом новой линии
plt.legend(fontsize=10)

# Подгоняем макет и показываем график
plt.tight_layout()
plt.show()












# Посчитаем базовую статистику по годам
# Добавляем столбец с годом
df_filtered['year'] = pd.DatetimeIndex(df_filtered['date']).year
# Группируем по годам и считаем статистику
yearly_stats = df_filtered.groupby('year')['co2_concentration'].agg(['mean', 'min', 'max', 'std'])
print("\nСтатистика по годам:")
print(yearly_stats.round(2))
print(f"\nОбщая статистика за период 1958-1980:")
print(f"Начальное значение: {df_filtered['co2_concentration'].iloc[0]:.2f} ppm")
print(f"Конечное значение: {df_filtered['co2_concentration'].iloc[-1]:.2f} ppm")
print(f"Общий рост: {df_filtered['co2_concentration'].iloc[-1] - df_filtered['co2_concentration'].iloc[0]:.2f} ppm")
print(f"Среднегодовой рост: {(df_filtered['co2_concentration'].iloc[-1] - df_filtered['co2_concentration'].iloc[0]) / (1980-1958):.2f} ppm/год")





