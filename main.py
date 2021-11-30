import pandas as pd
import statistics
import csv

import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
mathScore = df["math score"].to_list()

readingScore = df["reading score"].to_list()

mean = sum(mathScore)/len(mathScore)
median = statistics.median(mathScore)
mode = statistics.mode(mathScore)
std_dev = statistics.stdev(mathScore)
print(mean)
print(median)
print(mode)
print(std_dev)

fig = ff.create_distplot([mathScore],["result"],show_hist=False)

fstd_start,fstd_end = mean-std_dev, mean + std_dev
sstd_start,sstd_end = mean-(2*std_dev), mean + (2*std_dev)
tstd_start,tstd_end = mean-(3*std_dev), mean + (3*std_dev)



list_of_data_within_1_std_deviation = [result for result in mathScore if result > fstd_start and result < fstd_end]
list_of_data_within_2_std_deviation = [result for result in mathScore if result > sstd_start and result < sstd_end]
list_of_data_within_3_std_deviation = [result for result in mathScore if result > tstd_start and result < tstd_end]


print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(mathScore)))

print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(mathScore)))


print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(mathScore)))








