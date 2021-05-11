# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np 

veg_df = pd.read_csv(r'Datafiniti_Vegetarian_and_Vegan_Restaurants.csv')

veg_df_drop = ['claimed', 'descriptions.dateSeen', 'descriptions.sourceURLs', 'menus.category']
veg_df.drop(veg_df_drop, inplace=True, axis=1)
veg_df = veg_df.drop(columns=['menus.amountMax', 'menus.amountMin',
       'menus.currency',"menus.name", "postalCode"])
veg_df.drop_duplicates(inplace=True)

#for y in x.split array, check to see if y is inside is_vegan; everything inside of any is list interpretation 
veg_df["is_vegan"] = veg_df['categories'].apply(lambda x: any( 'Vegan' in y for y in x.split(','))) 
# print(veg_df["is_vegan"].value_counts()) #counts the unique values (2828 unique vegan values)
veg_df["is_vegetarian"] = veg_df['categories'].apply(lambda x: any( 'Vegetarian' in y for y in x.split(','))) #for y in x.split array, check to see if y is inside is_vegan
# print(veg_df["is_vegetarian"].value_counts()) #counts the unique values (6799 unique vegetarian values)
veg_df["is_both"] = (veg_df['is_vegan']) & (veg_df['is_vegetarian'])
# print(veg_df["is_both"].value_counts())

veg_df['cuisines'] = veg_df['cuisines'].apply(lambda x: x.split(','))
veg_df_exploded = veg_df.explode('cuisines')
len(veg_df["id"].unique()) 
a = veg_df[['categories', 'cuisines']]



