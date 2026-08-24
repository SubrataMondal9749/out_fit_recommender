

from recommend.outfit_recommend import recommend_class

def main():
  rec = recommend_class("data/outfits.csv")
  print("Outfit Recommendation for Color Red and Party Ocassion is : ")
  print(rec.recommend_func(color = "Red",ocassion = "Party"))

if __name__=="__main__":
  main()
  
  