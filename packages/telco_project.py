#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import seaborn as sns
import matplotlib.pyplot as plt

"""
Useful functions to handle outliers
"""


def kdeplot(data, x, hue):
    """
    Plot KDE of data grouped by hue
    """
    plt.figure(figsize=(15, 5))
    sns.kdeplot(data=data, x=x, hue=hue, shade=True)
    plt.title(f'Distribution of {x} grouped by {hue}')
    plt.xlabel(x)
    plt.ylabel(None)
    plt.yticks([])

    plt.show()


def impute_total_charges(data):
    """
    Impute missing values in a column with a value from another column
    """
    data['TotalCharges'] = data['TotalCharges'].fillna(data['MonthlyCharges'])

    return data
