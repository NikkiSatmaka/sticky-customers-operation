#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

"""
Useful functions to handle missing values
"""


def prepare_imputation(data, variable, *args):
    """
    Prepare data for imputation
    
    Parameters
    ----------
    data : pandas.DataFrame
        Dataframe to be prepared for imputation
    variable : list
        List of columns to be imputed
    *args :
        List of special keywords representing the missing values

    Returns
    -------
    pandas.DataFrame
        Dataframe prepared for imputation
    """
    
    if data is None or variable is None:
        raise ValueError('data and variable must be specified')

    # replace missval with nan for features in impute_cols
    for col in variable:
        for missval in args:
            data[col] = data[col].replace(missval, np.nan)
    
    return data


def impute_na(data, variable, mean_value, median_value):
    """
    Function to Fill Missing Values with Zeroes, Mean, and Median

    Parameters
    ----------
    data : pandas.DataFrame
        Dataframe to be imputed
    variable : str
        Column to be imputed
    mean_value : float  
        Mean value to be used for imputation
    median_value : float
        Median value to be used for imputation

    Returns
    -------
    pandas.DataFrame
        Dataframe with imputed values
    """

    data[variable+'_mean'] = data[variable].fillna(mean_value)
    data[variable+'_median'] = data[variable].fillna(median_value)
    data[variable+'_zero'] = data[variable].fillna(0)

    return data


def impute_total_charges(data):
    """
    Impute missing values in a column with a value from another column

    Parameters
    ----------
    data : pandas.DataFrame
        Dataframe to be imputed

    Returns
    -------
    pandas.DataFrame
        Dataframe with imputed values
    """
    data['TotalCharges'] = data['TotalCharges'].fillna(data['MonthlyCharges'])

    return data


def impute_no_phone_internet(data):
    """
    Handle cardinality of categorical features
    """
    data = data.replace('No internet service', 'No')
    data = data.replace('No phone service', 'No')

    return data
