from matplotlib import pyplot as plt
from collections import Counter

# Movies
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5,11,3,8,10]

print(range(len(movies)))
plt.bar(range(len(movies)),num_oscars)
plt.ylabel("Oscars")
plt.title("My fav movies")
plt.xticks(range(len(movies)),movies)
plt.show()

grades =[83,95,91,87,70,0,85,82,100,67,73,77,0]

# Grades
histogram = Counter(min(grade //10 * 10,90) for grade in grades)
plt.bar([x+5 for x in histogram.keys()],
        histogram.values(),
        10
        )
plt.axis([-5,105,0,5])
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decyl")
plt.ylabel("Num of students")
plt.title("Grades")
plt.show()