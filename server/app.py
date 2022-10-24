from flask import Flask,request,jsonify
from functools import cmp_to_key
import pytextrank,requests,spacy

from api import get_bill_data

with open("/usr/share/dict/words","r") as f:
  words = f.read().split("\n") + ["ukraine"]

EXCLUDED_WORDS = ["news"]

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("textrank")
def get_keywords(text):
  def compare_phrases(a,b):
    return -(a.rank * a.count - b.rank * b.count)
  doc = nlp(text)
  phrases = doc._.phrases
  phrases.sort(key=cmp_to_key(compare_phrases))

  ptexts = [phrase.text.lower() for phrase in phrases]
  seen = set()
  seen_add = seen.add
  ptexts = [pt for pt in ptexts if not (pt in seen or seen_add(pt))]
  ptexts = [pt for pt in ptexts if len([w for w in pt.split(" ") if w not in words or w in EXCLUDED_WORDS]) == 0]
  ptexts = [pt for pt in ptexts if len(pt) > 3]

  return ptexts[:10]

app = Flask(__name__)

@app.route("/req",methods=["POST"])
def data_request():
  rep_name = request.url.split("=")[1].replace("%20"," ")
  content = request.get_json(force=True)["content"]
  keywords = get_keywords(content)
  bills = ([],[])
  print(keywords)
  for keyword in keywords:
    if len(bills[0]) == 0:
      to_draw = 2
    else:
      to_draw = 1
    retr_bills = get_bill_data(keyword.split(" ")[0],rep_name,to_draw)
    bills = (
      bills[0] + retr_bills[0],
      bills[1] + retr_bills[1]
    )
    if len(bills[0]) >= 3:
      break

  response = jsonify(bills[0] + bills[1])
  response.headers.add("Access-Control-Allow-Origin","*")
  return response