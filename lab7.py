import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from time import perf_counter
import csv


def start():
    arr = np.array([5, 9, 10, 'ad', 7])
    arr = arr[::-1]
    print(arr)


def tableLoad():
    arr = np.genfromtxt('voltage.csv', delimiter=',')
    time = arr[:100, 0]
    time = time[:, np.newaxis]
    curr = arr[:100, 1]
    curr = curr[:, np.newaxis]
    volt = arr[:100, 2]
    volt = volt[:, np.newaxis]

    plt.plot(time, curr * 50, 'b', time, volt, 'r')
    plt.show()


def hist():
    arr = np.genfromtxt('test.csv', delimiter=',')
    arr = arr[1:]
    daysInYear = 365.25

    age = np.int_(arr[:, 1] / daysInYear)

    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot()
    ax.hist(age, 100, (50, 60))
    ax.grid()
    plt.show()


def plot3d():
    np.random.seed(40)
    xs = np.linspace(0, 10, 20)
    ys = xs
    zs = np.sin(xs)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, marker='x', c='red')
    plt.show()


def task1():
    arr1, arr2 = [], []
    n = 1000000
    for i in range(n):
        arr1.append(random.randrange(n))
        arr2.append(random.randrange(n))
    arr_start = perf_counter()
    arr3 = [arr1[i] * arr2[i] for i in range(n)]
    arr_duration = perf_counter() - arr_start
    np_arr1, np_arr2 = np.array(arr1), np.array(arr2)
    np_arr_start = perf_counter()
    np_arr3 = np.multiply(np_arr1, np_arr2)
    np_arr_duration = perf_counter() - np_arr_start
    print("Длительность поэлементного перемноения стандартных списков: ", arr_duration)
    print("Длительность поэлементного перемножения массивов NumPy:\t\t", np_arr_duration)


def task2():
    with open("data1.csv", mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        axes_names = []
        fst_plot_x, fst_plot_y, snd_plot_x, snd_plot_y = [], [], [], []
        for line in reader:
            if line[0] == 'Время':
                axes_names.append(line[0])
                axes_names.append(line[3])
                axes_names.append(line[17])
            else:
                fst_plot_x.append(float(line[0]))
                fst_plot_y.append(float(line[3]))
                snd_plot_x.append(float(line[0]))
                snd_plot_y.append(float(line[17]))
        plt.xlabel(axes_names[0])
        plt.ylabel(axes_names[1] + '/' + axes_names[2])
        plt.plot(fst_plot_x, fst_plot_y)
        plt.plot(snd_plot_x, snd_plot_y)
        plt.show()

        plt.xlabel(axes_names[1])
        plt.ylabel(axes_names[2])
        plt.plot(fst_plot_y, snd_plot_y, 'o')
        plt.show()


def task3():
    np.random.seed(40)
    xs = np.linspace(-5 * np.pi, 5 * np.pi, 100)
    ys = np.cos(xs)
    zs = np.sin(xs)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, marker='x', c='red')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


if __name__ == '__main__':
    # start()
    # tableLoad()
    # hist()
    # plot3d()
    # task1()
    # task2()
    task3()
