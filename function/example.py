import pandas as pd

def multiply_area_density_by_country_input(df):
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
    'Country': ["Canada", "USA", "Mexico"],
    'Area': [9, 7, 5],
    'Density' : [4, 10, 20]
})

multiply_area_density_by_country_input(df)
