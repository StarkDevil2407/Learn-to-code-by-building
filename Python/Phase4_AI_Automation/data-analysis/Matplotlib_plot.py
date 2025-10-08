import matplotlib.pyplot as plt

def simple_plot():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, marker='o', color='blue', label="Line Chart")
    plt.title("Simple Line Chart")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.legend()
    plt.grid(True)
    plt.show()

def bar_chart():
    fruits = ["Apple", "Banana", "Mango", "Orange"]
    sales = [30, 45, 15, 60]

    plt.figure(figsize=(6, 4))
    plt.bar(fruits, sales, color='green')
    plt.title("Fruit Sales")
    plt.xlabel("Fruit")
    plt.ylabel("Units Sold")
    plt.show()

if __name__ == "__main__":
    simple_plot()
    bar_chart()
