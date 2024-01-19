"""
Contains all the filter for your Datasets
"""
class FilteringClass:
    """
    Class for filtering
    """

    def __init__(self,df):
        self.df = df

    def filter_price(self, price):
        """
        Filter price
        """
        return self.df[self.df['Price Starting With ($)'] < price]
    
    def load_dataset(self, filename):
        """
        Function to Load Dataset
        """
        extension = filename.rsplit(".",1)[-1]
        if extension == "csv":
            return pd.read_csv(filename)
        else:
            raise TypeError(f"The extension is {extension} and not csv, Try Again")