from functools import cmp_to_key
import json,math,requests

def get_bill_data(keyword,person):
  with open("votes/search.json","r") as f:
    data = json.load(f)
  
  shortf = [bill for bill in data if keyword in bill["short_title"].lower() and "amendment" not in bill["short_title"].lower()]
  longf = [bill for bill in data if keyword in bill["title"].lower()]

  word_count = lambda x: len(x.split(" "))
  for bill in shortf:
    if word_count(bill["short_title"]) >= 12:
      shortf.remove(bill)
      longf.append(bill)

  def short_compare(a,b):
    stamp_diff = 2 * math.copysign(-(a["stamp"] - b["stamp"]),0)
    return stamp_diff + word_count(a["short_title"]) - word_count(b["short_title"])
  shortf.sort(key=cmp_to_key(short_compare))
  def long_compare(a,b):
    return -(a["stamp"] - b["stamp"])
  longf.sort(key=cmp_to_key(long_compare))

  selectable = (shortf + longf)[:2]
  recents = [bill for bill in selectable]
  recents.sort(key=cmp_to_key(long_compare))
  recents = recents[:1]
  selectable = [bill for bill in selectable if bill not in recents]
  selected = recents + selectable[:1]

  result = []
  for bill in selected:
    result.append({
      "bill": bill,
      "vote": get_vote_summary(bill,person)
    })
  return result

def get_vote_summary(bill,person):
  with open("votes/individual/%d-%d.json" % (bill["stamp"],bill["id"]),"r") as f:
    data = json.load(f)
  vote_data = data["results"]["votes"]["vote"]

  person_vote = None
  positions = vote_data["positions"]
  for item in positions:
    if item["name"] == person:
      person_vote = item["vote_position"]
      break
  
  return {
    "person": person_vote,
    "parties": {
      "democratic": vote_data["democratic"],
      "republican": vote_data["republican"],
      "independent": vote_data["independent"]
    }
  }
