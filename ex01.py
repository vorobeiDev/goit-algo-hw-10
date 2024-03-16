import pulp


model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

x1 = pulp.LpVariable("Лимонад", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Фруктовий_сік", lowBound=0, cat='Integer')

model += x1 + x2, "Загальна кількість продукції"

model += 2 * x1 + 1 * x2 <= 100, "Обмеження води"
model += 1 * x1 <= 50, "Обмеження цукру"
model += 1 * x1 <= 30, "Обмеження лимонного соку"
model += 2 * x2 <= 40, "Обмеження фруктового пюре"

model.solve()

print(f"Лимонаду потрібно виробити: {x1.varValue} одиниць")
print(f"Фруктового соку потрібно виробити: {x2.varValue} одиниць")
print(f"Максимальна загальна кількість продукції: {pulp.value(model.objective)} одиниць")