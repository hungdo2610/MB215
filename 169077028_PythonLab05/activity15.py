import matplotlib.pyplot as plt

def plot_line_chart():
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='b')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Line Graph")
    plt.grid(True)
    plt.show()

def plot_bar_chart():
    left_edges = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]

    plt.bar(left_edges, heights, width=8, color='g')
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.title("Bar Chart Example")
    plt.show()

def plot_pie_chart():
    values = [20, 60, 80, 40]
    labels = ["A", "B", "C", "D"]
    colors = ["red", "blue", "green", "orange"]

    plt.pie(values, labels=labels, autopct='%1.1f%%', colors=colors)
    plt.title("Pie Chart Example")
    plt.show()

def main():
    plot_line_chart()
    plot_bar_chart()
    plot_pie_chart()

if __name__ == "__main__":
    main()

