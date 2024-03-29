
from logging_handler import show_error_message
import pandas as pd
import misc_handler
from datetime import datetime



def replace_date(x):
    if "ago" in x:
        return datetime.now()
    else:
        return x

def clean_reviews_reddit(df):
    return_df=df.copy()
    return_df.drop_duplicates(inplace=True)
    if return_df.columns[0]=='Unnamed: 0': 
        return_df.pop(return_df.columns[0])
    return_df.columns=return_df.columns.str.replace(" ","_")
    return_df['Date']=pd.to_datetime(return_df['Date'])
    return return_df


def clean_reviews_gsm(df):
    return_df=df.copy()
    return_df.drop_duplicates(inplace=True)
    return_df.drop(columns='User location', inplace=True)
    return_df.columns=return_df.columns.str.replace(" ","_")
    return_df['Date']=return_df['Date'].apply(replace_date)
    return_df['Date']=pd.to_datetime(return_df['Date'])
    columns=['Product_id']
    return_df[columns]=return_df[columns].astype('int64')
    return return_df

def clean_specs(df):
    return_df=df.copy()
    return_df.columns=return_df.columns.str.replace(" ","_")
    return_df.columns=return_df.columns.str.replace(r'\.', '_', regex=True)
    return_df['Launch_Announced']=pd.to_datetime(return_df['Launch_Announced'])
    return_df.rename(columns={'Launch_Announced':'Release_Date'},inplace=True)   
    columns=['product_id']
    return_df[columns]=return_df[columns].astype('int64')
    return return_df

def clean_prices(df):
    all_prices=df.copy()
    all_prices.columns = all_prices.columns.astype(str)
    columns=list(all_prices.columns)
    for col in columns:
        if isinstance(col, str) and 'Unnamed' in col:
            all_prices.drop(columns=col, inplace=True)
        if isinstance(col, str) and 'Tests' in col:
            all_prices.drop(columns=col, inplace=True)
        if isinstance(col, str) and 'Misc' in col:
            all_prices.drop(columns=col, inplace=True)
        if isinstance(col, str) and 'nan' in col:
            all_prices.drop(columns=col, inplace=True)
    all_prices.columns=all_prices.columns.str.replace(" ","_")
    columns=['product_id']
    all_prices[columns]=all_prices[columns].astype('int64')
    new_column_names = ['_' + col if col != 'product_id' else col for col in all_prices.columns]
    all_prices.columns = new_column_names

    return all_prices

def clean_sales(df):
    return_df=df.copy()
    return_df.columns=['brand','sales','year']
    return return_df





