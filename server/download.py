import requests,json,os

def get_summary_for(year,month):
  print("Downloading %d-%d summary" % (year,month))
  data = requests.get(
    "https://api.propublica.org/congress/v1/house/votes/%d/%d.json" % (year,month),
    headers={"X-API-Key": "aFGV1lJG6sHwyMQBtKAhp2mumZlLlZ0OiISiPsqT"}
  ).json()
  with open("votes/summary/%d-%d.json" % (year,month),"w") as f:
    json.dump(data["results"]["votes"],f)

def get_search_table():
  table = []
  for file in os.listdir("votes/summary"):
    year = int(file.split("-")[0])
    month = int(file.split("-")[1].split(".json")[0])
    print("Processing %d-%d" % (year,month))
    with open("votes/summary/%s" % file,"r") as f:
      data = json.load(f)
    for item in data:
      if "title" not in item["bill"] or item["bill"]["title"] is None:
        continue
      table.append({
        "title": item["bill"]["title"],
        "short_title": item["description"],
        "vote_uri": item["vote_uri"],
        "id": int(item["vote_uri"].split("/")[-1].split(".")[0]),
        "stamp": year * 12 + month
      })
  print(len(table))
  with open("votes/search.json","w") as f:
    json.dump(table,f)

def get_individuals():
  existing = os.listdir("votes/individual")
  with open("votes/search.json","r") as f:
    data = json.load(f)
  for (index,bill) in enumerate(data):
    fname = "%d-%d" % (bill["stamp"],bill["id"])
    if fname + ".json" in existing:
      print("Skipping %s individual" % fname)
      continue
    print("Downloading %s individual (%d of %d)" % (fname,index + 1,len(data)))
    individual = requests.get(
      bill["vote_uri"],
      headers={"X-API-Key": "aFGV1lJG6sHwyMQBtKAhp2mumZlLlZ0OiISiPsqT"}
    ).json()
    with open("votes/individual/%s.json" % fname,"w") as f:
      json.dump(individual,f)

if __name__ == "__main__":
  """for year in range(2018,2022):
    for month in range(1,13):
      get_summary_for(year,month)
  for month in range(1,10):
    get_summary_for(2022,month)"""
  #get_search_table()
  get_individuals()