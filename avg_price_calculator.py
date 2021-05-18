# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np 

restaurant = pd.read_csv(r'Datafiniti_Vegetarian_and_Vegan_Restaurants.csv')

###copied and pasted from the restaurant_data_processing.opy script

restaurant["is_vegan"] = restaurant['categories'].apply(lambda x: any( 'Vegan' in y for y in x.split(','))) 
restaurant["is_vegetarian"] = restaurant['categories'].apply(lambda x: any( 'Vegetarian' in y for y in x.split(',')))
restaurant["is_both"] = (restaurant['is_vegan']) & (restaurant['is_vegetarian'])

veg_dict = {"Vegetarian,Indian":"Indian","Indian,Vegetarian":"Indian", "Mexican,Vegetarian":"Mexican","Vegetarian,Salads":"Unclassified", "Salads,Vegetarian":"Unclassified", "Vegetarian,Thai":"Thai", "Seafood,Vegetarian,Greek,Indian":"Greek and Indian","Middle Eastern,Lebanese,Mediterranean,Vegetarian Friendly,Vegan Options,Gluten Free Options":"Mediterranean",
            "Thai,Vegetarian":"Thai", "Thai,Asian/Pacific,Vegetarian":"Thai", "Asian,Thai,Vegetarian Friendly,Asian/Pacific,Fusion":"Thai","Mediterranean,Vegetarian":"Mediterranean", "Vegetarian,Mediterranean":"Mediterranean", "Vegetarian,International,Breakfast and Brunch,Vegan,Asian":"Asian",
            "Mediterranean,Vegetarian Restaurants":"Mediterranean", "Traditional American,Vegetarian":"American","American,Vegetarian":"American", "American,Ice Cream and Desserts,Vegetarian,Vegan":"American", "Thai,Thai Restaurants,Japanese,Asian,Sushi,Vegetarian Friendly,Vegan Options":"Thai and Japanese",
            "American,Seafood,Wine Bar,Vegetarian Friendly,Vegan Options,Gluten Free Options,Breakfast and Brunch,Bar,Soups":"American","New American,Traditional American,American,Vegetarian Friendly,Gluten Free Options,Vegan Options,Northwest, American":"American", "Mexican,Middle Eastern,Vegetarian,Turkish":"Mexican and Turkish",
            "Traditional American,Seafood,Vegetarian,Vegetarian Restaurants":"American", "American,Vegan,Gluten Free":"American", "American,Breakfast and Brunch,Cafe,Contemporary American, Vegetarian / Vegan, Global, International":"American", "Traditional American,Mexican,Vegetarian":"Mexican and American","Asian Fusion,Vegan":"Asian",
            "Traditional American,Seafood,Vegetarian,Hamburgers":"American", "American (New),Vegetarian,Coffee and Tea,Health Food,Vegan":"American", "Chain Restaurant,American , Fast Food , Health , Organic , Smoothies , Traditional , Vegan , Vegetarian , Specialties":"American", "Vegetarian,Chinese,Thai":"Chinese and Thai", "Vegan Restaurants,Caterers,Bakeries,Continental Restaurants,Breakfast Brunch and Lunch Restaurants,,Vegetarian Restaurants,Restaurants,Breakfast,Brunch and Lunch,European,Healthy,Vegetarian,Vegan,Continental":"European",
            "American,Vegetarian Friendly,Vegan Options,Gluten Free Options,Breakfast and Brunch":"American", "American Restaurants,Caterers,Coffee Shops,Vegetarian Restaurants,Vegan Restaurants,Breakfast Brunch and Lunch Restaurants,,Restaurants,American,Cafeterias,Breakfast,Brunch and Lunch,Healthy,Vegetarian,Vegan":"American", "American (New),Local/Organic,Vegetarian":"American", "American,Vegetarian Friendly,Gluten Free Options,Vegan Options":"American","Traditional American,American,Soups,Vegetarian Friendly,Vegan Options,Gluten Free Options":"American", "Barbecue Restaurants,American, Vegetarian":"American","Mediterranean,Vegetarian,Persian,Middle Eastern":"Middle Eastern",
            "Healthy,Salad,Breakfast and Brunch,American,Soups,Vegetarian Friendly,Vegan Options,Gluten Free Options":"American", "Traditional American,Vegan,Breakfast and Brunch,Vegan Options":"American","American (New),New American,Local/Organic,Vegetarian":"American", "Southern / Soul,Vegetarian,Breakfast and Brunch,Vegan,American Restaurants,Caterers,Restaurants":"American", 
            "Mexican Restaurants,Latin American Restaurants,Vegetarian Restaurants,Vegan Restaurants,Caterers,Restaurants,Mexican,Latin American,Healthy,Vegetarian,Vegan":"Mexican", "Mexican,Vegetarian,Breakfast and Brunch,Diners":"Mexican", "Mexican Restaurants,Latin American Restaurants,American Restaurants,Vegetarian Restaurants,Seafood Restaurants,Vegan Restaurants,Bar and Grills,Restaurants,Mexican,American,Latin American,Seafood,Healthy,Vegetarian,Vegan":"American", 
            "Mexican,Seafood,Vegetarian,Southwestern":"American", "Vegetarian,Indian,Desserts":"Indian", "Deli Food,Vegetarian,Indian":"Indian", "Indian Restaurants,Caterers,Restaurants,Indian,Indian, Vegan":"Indian","Indian Restaurants,Middle Eastern Restaurants,Asian Restaurants,Vegetarian Restaurants,Vegan Restaurants,Restaurants,Asian,Indian,Healthy,Vegetarian,Middle Eastern,Vegan":"Indian",
            "Indian,Indian, Vegetarian, Bar / Lounge / Bottle Service":"Indian", "Vegetarian,Indian, Vegetarian-Friendly,Indian":"Indian", "Indian,Vegetarian,Take Out Restaurants":"Indian","Indian,Vegetarian Friendly,Vegan Options,Gluten Free Options,Indian Restaurants":"Indian", "Italian,American,Bar,Vegetarian Friendly,Gluten Free Options,Vegan Options":"Italian", 
            "Italian,Vegetarian":"Italian", "New American,Vegetarian,Italian":"Italian", "Seafood,Italian,Vegetarian,Deli and Sandwich":"Italian", "Pizza,Restaurants,Italian,Vegetarian Friendly":"Italian", "Vegetarian,Italian,Pizza":"Italian", "American,Italian,Healthy,Vegetarian":"Italian", "Italian, Vegetarian,Italian":"Italian", "Ethiopian,Vegetarian":"Ethiopian",
            "Italian,Pizza,Vegetarian":"Italian", "Vegetarian,Chinese":"Chinese", "Chinese,Vegetarian":"Chinese", "Asian/Pacific,Health Food,Vegetarian,Chinese":"Chinese", "Vegetarian,Chinese,Chinese Restaurants":"Chinese", "Chinese Restaurants,Caterers,Bars,Asian Restaurants,Bar and Grills,Vegan Restaurants,Restaurants,Asian,Healthy,Chinese,Vegetarian,Vegan,Taverns":"Chinese",
            "Cocktails,Vegetarian,Dim Sum,Chinese":"Chinese", "Vegetarian,Dim Sum,Chinese":"Chinese", "Vegetarian,Japanese,Noodles":"Japanese", "Vegetarian,Sushi,Japanese":"Japanese", "Japanese,Sushi,Vegetarian":"Japanese", "Vegetarian,Japanese,Healthy":"Japanese", "Asian,Sushi,Japanese,Seafood,Vegetarian":"Japanese", "Vegetarian,Breakfast and Brunch":"Unclassified",
            "Fast Food,Japanese,Asian,Vegetarian Friendly,Vegan Options":"Japanese", "Asian,Sushi,Japanese,Vegetarian,Steakhouse":"Japanese", "Vegetarian,Sushi,Kosher,Japanese":"Japanese", "Middle Eastern,Vegetarian":"Middle Eastern", "Middle Eastern,Sandwiches,Vegetarian":"Middle Eastern","Pizza,Middle Eastern,Vegetarian,Salads,Kosher":"Middle Eastern", "Mediterranean,Mediterranean Restaurants,Middle Eastern,Lebanese,Greek,Vegetarian Friendly,Vegan Options":"Mediterranean",
            "Middle Eastern,Smoothies and Juices,Vegetarian":"Middle Eastern", "Middle Eastern and African,Mediterranean,Health Food,Vegan,Vegetarian":"Middle Eastern", "Middle Eastern,Middle Eastern, Vegetarian-Friendly,Vegetarian":"Middle Eastern","Middle Eastern,Vegetarian,Sandwiches":"Middle Eastern", "Vegetarian,Hot Dogs":"Americans", "Americans":"American", "Southern,Vegetarian":"American", "Vegetarian,Healthy":"Unclassified", "Thai,Southeast Asian,Asian,Vegetarian":"Thai", "Vegetarian,Sandwiches":"Unclassified", "Health Food,Vegetarian,Hamburgers":"Unclassified", "Vegan,Take Out Restaurants":"Unclassified", "Vegetarian,Californian":"American", 
            "French,Vegetarian":"French", "French,Vegetarian,French, Continental, American":"French", "French,Vegetarian,Bistro":"French", "Vegetarian Restaurants":"Unclassified", "Southeast Asian,Vegetarian,Korean":"Korean", "Vegetarian,Korean":"Korean", "Vegetarian,Greek":"Mediterranean", "Mediterranean Restaurants,Greek Restaurants,Restaurants,Greek,Fast Food,Mediterranean,Vegetarian Friendly,Vegan Options":"Mediterranean", 
            "Greek,Vegetarian":"Mediterranean", "New American,Health Food,Vegan,Vegetarian,Greek,Mediterranean,Tapas / Small Plates":"Mediterranean", "Greek,Seafood,Mediterranean,Vegetarian,Mediterranean Restaurants":"Mediterranean", "Health Food,Vegetarian":"Unclassified", "Vegetarian,Vietnamese":"Vietnamese", "Asian Restaurants,Take Out,Vietnamese Restaurants,Vegetarian,Take Out Restaurants,Vietnamese,Asian,Restaurants,Vegan":"Vietnamese",
            "Pizza,Pizza, Kosher, Vegetarian-Friendly,Vegetarian,Kosher":"Kosher", "Vegetarian,Eclectic and International,Kosher,Vegan":"Kosher", "Sushi,Kosher,Vegan":"Kosher", "Pizza,Vegetarian,Kosher":"Kosher", "Local/Organic,Smoothies and Juices,Vegetarian,Kosher,Healthy,Vegan":"Kosher", "Vegetarian,Kosher,Sandwiches,Kosher, Vegetarian-Friendly, Sandwiches":"Kosher", "Eastern European,Kosher,Vegetarian":"Kosher", "Mediterranean,Vegetarian,Coffee and Tea,Kosher":"Mediterranean",
            "Local/Organic,Vegetarian,Coffee and Tea,Vegan":"Unclassified", "Breakfast and Brunch,Vegan":"Unclassified", "Vegetarian,Indian,Vegetarian Restaurants":"Indian", "Vegetarian,Coffee and Tea":"Unclassified", "Ice Cream and Desserts,Breakfast and Brunch,Coffee and Tea,Vegan,Vegetarian":"Unclassified", "Smoothies and Juices,Vegetarian,Coffee and Tea,Healthy,Vegan":"Unclassified", "Desserts,Bakery and Pastries,Vegan":"Unclassified", "Hamburgers,Vegetarian":"Unclassified",
            "Vegetarian,African":"African","Vegetarian,Tapas / Small Plates":"Unclassified", "Traditional American,Health Food,Vegetarian":"American", "Coffee Shops,Delicatessens,Coffee and Espresso Restaurants,Vegan Restaurants,Restaurants,Vegetarian,Coffee and Tea,Vegan":"Unclassified", "Smoothies and Juices,Vegetarian,Healthy":"Unclassified", "Vegetarian,Caterers":"Unclassified", "Local/Organic,Smoothies and Juices,Vegetarian,Healthy,Vegan":"Unclassified", "Local/Organic,Vegetarian,Coffee and Tea,Healthy,Vegan":"Unclassified",
            "Vegetarian,Coffee and Tea,Bakery,Desserts,Bakery and Pastries,Vegan":"Unclassified", "Vegetarian,Soups":"Unclassified", "American, Mexican, Vegetarian":"Mexican", "Vegetarian,Vegetarian Restaurants":"Unclassified", "Persian,Vegetarian Restaurants":"Middle Eastern", "British (Modern),Vegetarian":"British", "Local/Organic,Vegan Restaurants,Smoothies and Juices,Vegetarian,Healthy":"Unclassified", "Pizza,Middle Eastern,Lebanese,Vegetarian":"Middle Eastern", "Vegetarian,Breakfast and Brunch,Vegetarian Friendly,Juices":"Unclassified",
            "Health Food Restaurants,Delicatessens,Sandwich Shops,Vegetarian Restaurants,Vegan Restaurants,Restaurants,Take Out Restaurants":"Unclassified", "Breakfast and Brunch,Vegetarian,Coffee and Tea,Hungarian,Healthy,Vegan":"Hungarian", "Middle Eastern and African,Mediterranean,Vegetarian,Lebanese":"Mediterranean", "Vegetarian,Chinese,Dim Sum,Thai":"Chinese and Thai", "Pizza,Middle Eastern,Lebanese,Vegetarian":"Middle Eastern"}

for original, replacer in veg_dict.items():
    restaurant['cuisines'] = restaurant['cuisines'].replace([original],replacer)
print(restaurant['cuisines'].value_counts())

dietary = []

i = 0
while i < restaurant.shape[0]:
    if restaurant["is_vegan"][i] == True:
        dietary.append("vegan")
    elif restaurant["is_vegetarian"][i] == True:
        dietary.append("vegetarian")
    else:
        dietary.append("neither")
    i+=1

restaurant["dietary"] = dietary
restaurant = restaurant[restaurant["dietary"]!="neither"]

### price calculation
# priceMean = restaurant.pivot_table(index=["cuisines", "dietary"], values = ["menus.amountMax"], aggfunc = "mean")
priceMean = restaurant.pivot_table(index=["cuisines"], columns=["dietary"], values = ["menus.amountMax"], aggfunc = "mean")

priceMean.to_csv(r'price_mean_data_pivot2.csv')

priceMean.to_json(r'price_mean_data_json.json',orient="index")
    

    
    