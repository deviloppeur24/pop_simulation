import pandas as pd

def game_function(df):
    print("Demographic Simulation Game\n") 

    country1 = input("Enter a country : ")
    
    if country1 not in df['Country'].values:
        print(f"The country '{country1}' does not exist in the DataFrame.")
        return
    
    area = df.loc[df['Country'] == country1, 'Area'].iloc[0]

    country2 = input("Enter an other country : ")
    
    if country2 not in df['Country'].values:
        print(f"The country '{country2}' does not exist in the DataFrame.")
        return
    
    density = df.loc[df['Country'] == country2, 'Density'].iloc[0]
    
    result = area * density
    
    print(f"The population of {country1} if it had the population density of {country2} would be: {result} inhabitants")

df = pd.DataFrame({
    'Country': ["Canada", "USA", "Mexico", "China", "Spain"],
    'Area': [9900000, 9800000, 1900000, 9600000, 500000],
    'Density' : [4, 35, 65, 149, 94]
})

game_function(df)

