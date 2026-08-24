

class recommend_class:
  def __init__(self,csv_file):
    import pandas as pd

    self.data = pd.read_csv(csv_file)
  
  
  def recommend_func(self,color = None,ocassion = None):
    result = self.data
  
    if color:
      result = result[result['color'].str.lower() == color.lower()]
    if ocassion:
      result = result[result['ocassion'].str.lower() == ocassion.lower()]

    return result['outfits'].tolist()
  
  
  