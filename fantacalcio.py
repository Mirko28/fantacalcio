from lxml import html
import requests, string
from yourteam import squadra

page = requests.get('https://www.pianetafantacalcio.it/Voti-Ufficiosi-Mondiale.asp')
tree = html.fromstring(page.content)
giocatori = tree.xpath('//a[@class="linktabelle"]/text()')
voti = tree.xpath('//td[@class="fantat"]/text()')
tot = 0.0 
for index in range(len(squadra)):
	giocatore = squadra[index]
	for i in range(len(giocatori)):
		if giocatore == giocatori[i]:
			voti[i] = voti[i].strip()
			voti[i] = voti[i].replace(',', '.')
			print ('\n' + str(index+1) + ') '+ giocatore + ' ' + voti[i])
			print ('-----------------------')
			tot = tot + float(voti[i])

print ('\nTOT: ' + str(tot))