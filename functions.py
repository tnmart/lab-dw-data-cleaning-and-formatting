
import pandas as pd

def columns_lowercase(dataframe: pd.DataFrame) ->pd.DataFrame:
    '''
    Changes column names in a dataframe to lowercase.
        
    Inputs:
    dataframe: Pandas DataFrame
    
    Outputs:
    dataframe: Pandas DataFrame
    '''
    
    dataframe2 = dataframe.copy()
    cols = []
    for col in dataframe2.columns:
        cols.append(col.lower())
    dataframe2.columns = cols
    return dataframe2

def replace_whitespaces_column_names(dataframe: pd.DataFrame) ->pd.DataFrame:
    '''
    Replaces white spaces by underscores in all column names of a dataframe
    
    Inputs:
    dataframe: Pandas DataFrame
    
    Outputs:
    dataframe2: Pandas DataFrame
    '''
    
    dataframe2 = dataframe.copy()
    dataframe2.columns = dataframe2.columns.str.replace(' ', '_')
    return dataframe2

def drop_missing_values(dataframe: pd.DataFrame)->pd.DataFrame:   
    '''
    Drops rows which have only columns with missing values
    
    Inputs:
    dataframe: Pandas dataFrame
    
    Outputs:
    dataframe2: Pandas dataFrame
    '''
    
    dataframe2 = dataframe.copy()
    dataframe2.dropna(axis=0, how="all",inplace=True)
    dataframe2.reset_index()
    return dataframe2

def clean_database(dataframe: pd.DataFrame)->pd.DataFrame:
    '''
    This function applies previous functions in the library to format and clean a Pandas dataframe.
    
    Inputs:
    dataframe: Pandas dataFrame
    
    Outputs:
    dataframe2: Pandas dataFrame
    '''
    
    dataframe2 = dataframe.copy()
    dataframe2 = columns_lowercase(dataframe2)
    dataframe2 = replace_whitespaces_column_names(dataframe2)
    dataframe2 = drop_missing_values(dataframe2)
    return dataframe2
