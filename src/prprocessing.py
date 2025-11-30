import pandas as pd


class preprocessor:
    def __init__(self, data: pd.DataFrame):
        self.housing = data
        pass



    def amenities_value(self):
        self.housing["Amenities_value"] = self.housing["Amenities"].apply(lambda x: len(x.split(", ")))
        return self


