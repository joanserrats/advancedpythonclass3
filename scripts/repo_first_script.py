"""
Script to make updates in github
"""

import pandas as pd
import click

class FilteringClass:
    """
    Class for filtering
    """

    def _init_(self,df):
        self.df = df

    def filter_price(self, price):
        """
        Filter price
        """
        return self.df[self.df['Price Starting With ($)'] < price]
    

def load_dataset(filename):
    """
    function to load dataset
    """
    extension = filename.rsplit('.', 1)[-1]
    if extension == "csv":
        return pd.read_csv(filename)
    else:
        raise TypeError(f"The extension is {extension} and not csv. Try again")

@click.command(short_help='Parser to import datset')
@click.option('-f', '--file_name', required=True, help='File to import')
def main(file_name):
    """
    Main function
    """
    df = load_dataset(input_file)
    
    
    result = FilteringClass(df).filter_price(12)
    
    print(result.shape)

if __name__ == "__main__":
    main()