


# Homework 1 7711


## Installation and Running

Written in Python3 and requires Python package matplotlib

Typing `pip freeze` will tell you which packages you have installed.
If you do not have matplotlib installed, please install it.

run `python3 hw1.py`

If you have any questions about running this program, please contact
jennifer dot harper @ucdenver.edu or ping me on the CPBS Slack channel.

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

#### Formulas:

**ACCURACY:**

accuracy = (TP + TN)/(TP + TN + FP + FN)

**F-SCORE:**

f_score = 2*((precision * recal)/(precision + recall))

precision = TP/(TP + FP)

recall = TP/(TP + FN)

