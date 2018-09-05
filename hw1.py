
"""
## Original Directions

1.  Simulate the effect of rare events on accuracy and F-measure:
    Write a program that shows how the accuracy and F-measure
    change if you keep the number of TP, FP, and FN constant, but
    increase the number of TNs.

    So, the x-axis will be the count of
    TNs, and the y-axis will show accuracy and F-measure. (Hint:
    sketch out what you expect this to look like.)

2.  Check your work into GitHub, including your graph.

3.  Check out a classmate’s code and run it. Write down everything
    that you had to fix to get it to run and produce output for you.

**ACCURACY:**

accuracy = (TP + TN)/(TP + TN + FP + FN)

**F-SCORE:**

f_score = 2*((precision * recal)/(precision + recall))

precision = TP/(TP + FP)

recall = TP/(TP + FN)

"""
import matplotlib.pyplot as plt

# constants
tp = 1
fp = 1
fn = 1

# variable
tn = 1

tn_list = []
accuracy_list = []
f_score_list = []

for i in range(1, 50):

    # increment true negatives for x-axis
    tn += i
    tn_list.append(tn)

    # create accuracy list for y-axis
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    accuracy_list.append(accuracy)

    # create f-score list for y-axis
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    f_score = 2*((precision*recall)/(precision + recall))
    f_score_list.append(f_score)

# plot
figure = plt.scatter(tn_list, accuracy_list, label="Accuracy", c="orchid", s=50)
figure = plt.scatter(tn_list, f_score_list, label="F-score", c="cyan", s=50)
figure = plt.xlabel("True Negatives")
figure = plt.legend(loc=5)
plt.show()