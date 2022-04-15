'''These functions are custom built for the data preprocessing as per the model selected.'''

def DataPreprocessingXGB(dff):

    df_copy = dff.copy()
    drop_columns = ['cid', 'dayhours'] #delete the cid, dayhours columns
    df_copy.drop(drop_columns, inplace=True, axis=1)
    sel_cols = ('yr_renovated', 'living_measure', 'ceil_measure', 'furnished', 'sight',
        'quality', 'lot_measure15', 'yr_built', 'room_bath', 'coast',
        'living_measure15', 'long', 'zipcode', 'lat')
    df = df_copy.loc[:, sel_cols]

    cols_list = list(df.columns)
    #change the first and last column names below as required
    start_column = cols_list.index('yr_renovated')
    end_column   = cols_list.index('lat')

    #change dtype from object to int
    for index, col in enumerate(cols_list):
        if (start_column <= index) & (index <= end_column):
            df[col] = df[col].astype(float)

    return df


def DataPreprocessingRFG(dff):

    df_copy = dff.copy()
    drop_columns = ['cid', 'dayhours'] #delete the cid, dayhours columns
    df_copy.drop(drop_columns, inplace=True, axis=1)
    sel_cols = ('yr_renovated', 'living_measure', 'furnished', 'quality', 'yr_built',
        'room_bath', 'coast', 'long', 'zipcode', 'lat')
    df = df_copy.loc[:, sel_cols]

    cols_list = list(df.columns)
    #change the first and last column names below as required
    start_column = cols_list.index('yr_renovated')
    end_column   = cols_list.index('lat')

    #change dtype from object to int
    for index, col in enumerate(cols_list):
        if (start_column <= index) & (index <= end_column):
            df[col] = df[col].astype(float)

    return df



