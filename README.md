# Frequent Itemsets and Association Rules

This mini-project is done by Candace Chou (me) and Nihad Ibrahimli.

## Introduction

Run :
``` python3 main.py ```


First of all,  the user tells us the support threshold (s) and the confidence
threshold (c), then the dataset, which records the content of baskets line by line, is read to record the frequncy of each item.

We  calculate the frequency of appearance of each  items appear in the file and apply the associate rule to find the frequent itemsets.

After finished, a Report.txt file is generated record the frequent items.

## some experiments

with s = 500

    |Bought together |c=0.3|c=0.5|c=0.7|c=0.9|
    |----------------|-----|-----|-----|-----|
    | 1 item  | 569  | 569 | 569 |  569  |
    | 2 items |  35  |  5  | 1 |   0 |
    | 3 items |  5  |   1  | 0 |   0 |
    | 4 items |  0 |   0   | 0 |   0 |

