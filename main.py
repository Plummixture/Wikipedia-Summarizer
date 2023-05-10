import requests, os, openai
from bs4 import BeautifulSoup
from replit import db


#div
#mw-parser-output
#p
#references
#ol
#db['API']['orgID']
#db['API']['openai']


openaikey = os.environ['openaikey']
orgID = os.environ['orgID']

openai.organization = orgID
openai.api_key = openaikey
openai.Model.list()


url = input("Input Wikipedia URL: ").strip()
print('\n')
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

try:
  article = soup.find_all('div', {'class': "mw-parser-output"})[1]
except:
  article = soup.find_all('div', {'class': "mw-parser-output"})[0]  
  
content = article.find_all('p')

count = 0
text = ''
for i in content:
  if count < 20:
    text += i.text
    count += 1

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f'Summarize {text} in one paragraph.',
    max_tokens=250,
    temperature=0
  )

print(response['choices'][0]['text'].strip())

#refs = soup.find_all('ol', {'class': 'references'})
#for i in refs:
  #print(i.text.replace('^ ', ''))

