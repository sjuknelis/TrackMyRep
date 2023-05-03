from flask import Flask,request,jsonify
from flask_cors import CORS,cross_origin
from functools import cmp_to_key
from itertools import chain
import pytextrank,spacy,time

from api import get_bill_data

EXCLUDED_WORDS = ["news","day","days","next","few","monday","tuesday","wednesday","thursday","friday","saturday","sunday","january","february","march","april","may","june","july","august","september","october","november","december","congress","law","court","president","trump","biden","obama","house","senate","hill","democrat","democratic","republican","republic","progressive","conservative","year","agency","authorization"]
INCLUDED_WORDS = ["ukraine","ACTED","ADRA","AIESEC","CAFOD","CRS","Koyamada","Oxfam","Narayan","Tzu","Chi","Amref","GAVI","FIMCAP","WAGGGS","WOSM","INGO","COSPAR","RIPE NCC","IMIRAD"]
with open("countries.txt","r") as f:
  countries = f.read().split("\n")
  INCLUDED_WORDS += list(chain.from_iterable([country.split(" ") for country in countries]))
with open("/usr/share/dict/words","r") as f:
  words = f.read().split("\n") + INCLUDED_WORDS

DAY = 24 * 60 * 60
last_downloaded = 0

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
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/req",methods=["POST"])
def data_request():
  rep_name = request.url.split("=")[1].replace("%20"," ")
  content = request.get_json(force=True)["content"]
  keywords = get_keywords(content)
  print(keywords)

  searched = []
  bills = ([],[])
  for keyword in keywords:
    search = keyword.split(" ")[-1]
    if search in searched:
      continue
    searched.append(search)

    retr_bills = get_bill_data(search,rep_name,3)
    print(keyword,len(retr_bills[0]))
    bills = (
      bills[0] + retr_bills[0],
      bills[1] + retr_bills[1]
    )
    if len(bills[0]) >= 3:
      break
  
  if len(searched) == 1:
    for keyword in keywords:
      search = keyword.split(" ")[-1]
      if search in searched:
        continue
      searched.append(search)

      retr_bills = get_bill_data(search,rep_name,3)
      print(keyword,len(retr_bills[0]))
      if len(retr_bills[0]) == 3:
        bills = (
          bills[0][:2] + [retr_bills[0][0]],
          bills[1][:2] + [retr_bills[1][0]]
        )
      break

  global last_downloaded
  if time.time() > last_downloaded + DAY:
    #os.system("python download.py &")
    last_downloaded = time.time()

  print(len(bills[0]),len(bills[1]))
  return jsonify([bills[0],bills[1]])

@app.route("/test",methods=["GET"])
def test():
  return "hi"