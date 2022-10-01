from flask import Flask,request,jsonify
from functools import cmp_to_key
import pytextrank,requests,spacy

from api import get_bill_data

with open("/usr/share/dict/words","r") as f:
  words = f.read().split("\n")

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
  ptexts = [pt for pt in ptexts if len([w for w in pt.split(" ") if w not in words]) == 0]

  return ptexts[:10]

app = Flask(__name__)

@app.route("/req",methods=["POST"])
def data_request():
  content = request.get_json(force=True)["content"]
  keywords = get_keywords(content)
  bills = []
  print(keywords)
  for keyword in keywords[:3]:
    bills += get_bill_data(keyword.split(" ")[0],"Katherine Clark")

  print(bills)
  response = jsonify(bills)
  response.headers.add("Access-Control-Allow-Origin","*")
  return response