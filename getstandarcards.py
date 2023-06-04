import requests
import json

# bulk data link
link = 'https://api.scryfall.com/bulk-data'

res = requests.get(link)

response = json.loads(res.text)

# Get the default cards download link
link_defaultcards = ''
for obj in response['data'] :
    
    if obj['name'] == 'Default Cards':
        link_defaultcards = obj['download_uri']
        break

# Download all the default cards
res_bulk = requests.get(link_defaultcards)
all_cards = json.loads(res_bulk.text)

# Filter out the stuff we dont need
standard_cards = []
standard_card_names = []
for card in all_cards:
    if 'type_line' in card:
        if 'Basic Land' in card['type_line']:
            continue
    else:
        continue
    
    # Check if card is legal in standard
    if card['legalities']['standard'] == 'legal':
        
        # There are multiple versions of cards. If we already have it don't keep another.
        # For example there are 14 versions of Abrade. Just the one will do.
        if card['name'] in standard_card_names:
            continue
        else:
            standard_cards.append(card)
            standard_card_names.append(card['name'])
        
# Sort the cards into alphbetical order
standard_cards = sorted(standard_cards, key= lambda card: card['name'])

# Write the standard cards to a json file
standard_cards_json = json.dumps(standard_cards, indent=4)
with open('standard_cards.json', 'w') as output:
    output.write(standard_cards_json)