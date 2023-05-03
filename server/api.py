from functools import cmp_to_key
import json,math,requests
from sklearn.metrics import recall_score

def get_bill_data(keyword,person,to_draw):
  with open("votes/search.json","r") as f:
    data = json.load(f)
  
  def get_question(bill):
    with open("votes/individual/%d-%d.json" % (bill["stamp"],bill["id"]),"r") as f:
      data = json.load(f)
    return data["results"]["votes"]["vote"]["question"]

  shortf = [(bill,get_question(bill)) for bill in data if keyword in bill["short_title"].lower() and "amendment" not in bill["short_title"].lower() and "consideration" not in bill["short_title"].lower()]

  word_count = lambda x: len(x.split(" "))
  for (bill,question) in shortf:
    if word_count(bill["short_title"]) >= 12:
      shortf.remove((bill,question))

  def passage_sort(a,b):
    a_bill,a_question = a
    b_bill,b_question = b
    a_val = 1 if a_question == "On Passage" else 0
    b_val = 1 if b_question == "On Passage" else 0
    return -(a_val - b_val)
  def short_compare(a,b):
    if passage_sort(a,b) != 0:
      return passage_sort(a,b)
    a_bill,a_question = a
    b_bill,b_question = b
    stamp_diff = 2 * math.copysign(-(a_bill["stamp"] - b_bill["stamp"]),0)
    return stamp_diff + word_count(a_bill["short_title"]) - word_count(b_bill["short_title"])
  shortf.sort(key=cmp_to_key(short_compare))
  def long_compare(a,b):
    if passage_sort(a,b) != 0:
      return passage_sort(a,b)
    a_bill,a_question = a
    b_bill,b_question = b
    return -(a_bill["stamp"] - b_bill["stamp"])

  short_titles = [bill["short_title"] for (bill,question) in shortf]
  to_remove = []
  for (index,(bill,question)) in enumerate(shortf):
    if short_titles.index(bill["short_title"]) != index:
      to_remove.append((bill,question))
  for item in to_remove:
    shortf.remove(item)

  relevant = shortf[:to_draw]
  recent_selectable = shortf[to_draw:10]
  recent_selectable.sort(key=cmp_to_key(long_compare))
  recent = recent_selectable[:to_draw]

  result = ([],[])
  for (bill,question) in relevant:
    result[0].append({
      "bill": bill,
      "question": question,
      "vote": get_vote_summary(bill,person)
    })
  for (bill,question) in recent:
    result[1].append({
      "bill": bill,
      "question": question,
      "vote": get_vote_summary(bill,person)
    })
  return result

  """selectable = shortf[:3]
  recent = [item for item in selectable]
  recent.sort(key=cmp_to_key(long_compare))
  recent = recent[:to_draw]
  selectable = [(bill,question) for (bill,question) in shortf if (bill,question) not in recent and bill["short_title"] not in [jbill["short_title"] for (jbill,jquestion) in recent]]
  relevant = selectable[:to_draw]
  result = ([],[])
  for (bill,question) in recent:
    result[0].append({
      "bill": bill,
      "question": question,
      "vote": get_vote_summary(bill,person)
    })
  result = ([],[])
  for (bill,question) in relevant:
    result[1].append({
      "bill": bill,
      "question": question,
      "vote": get_vote_summary(bill,person)
    })
  return result"""

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
