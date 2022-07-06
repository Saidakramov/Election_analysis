from dataclasses import dataclass


print("Hello World!")
counties_dict = {}
counties_dict["Arapahoe"]= 422829
counties_dict
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict
len(counties_dict)
counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.get("Denver")

voting_data =[]
voting_data.append({"county":"Arapahoe", "registered_voters":422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.insert(1,{"county":"El Paso", "registered_votres":461149})
voting_data.pop(0)
voting_data