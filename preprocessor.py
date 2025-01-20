import pandas as pd

def preprocess(df, region_df):
    # Filter for summer Olympics
    df = df[df['Season'] == 'Summer']
    
    # Rename conflicting columns in region_df to avoid duplicates
    region_df.rename(columns={'region': 'region_name', 'notes': 'region_notes'}, inplace=True)
    
    # Merge with region_df
    df = df.merge(region_df, on='NOC', how='left')
    
    # Ensure 'region_name' exists even if some rows lack regions
    df['region_name'] = df['region_name'].fillna('Unknown')
    
    # Drop duplicates
    df.drop_duplicates(inplace=True)
    
    # One-hot encoding for medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    
    return df
