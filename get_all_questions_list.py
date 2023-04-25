import requests
import json
from bs4 import BeautifulSoup
from QuestionFetcher import QuestionFetcher 
import asyncio


url = "https://leetcode.com/api/problems/all/"
response = requests.get(url)
data = response.json()
questions_list = data['stat_status_pairs']

report = {
    'success':[],
    'fail':[]
    
}

for qstn in questions_list:
    qstn_slug = qstn['stat']['question__title_slug']
    qstn_id = ("00000" + str(qstn['stat']['question_id']))[-4:]
    try:
        
        QuestionFetcher.execute(qstn_slug, f"questions/{QuestionFetcher.clean_name(f'{qstn_id} - {qstn_slug}')}")

        report['success'].append(qstn_id)
    except Exception as e:
        report['fail'].append(qstn_id)

with open("json_file.json", "w") as outfile:
    json.dump(report, outfile)
