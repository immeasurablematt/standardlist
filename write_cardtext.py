import json
import os
import textwrap

with open('standard_cards.json') as file:
    cards = json.load(file)
    
def write_cardside(card, back=False):
    # Gets the text and formats a string to write for a single side of a card
    
    line1 = f'{card["name"]} {card["mana_cost"]}'
    line2 = f'\n{card["type_line"]}'
    
    # Some cards have no text. e.g. basic creatures
    line3 =''
    if len(card['oracle_text']) > 0:
        line3 = f'\n{card["oracle_text"]}'
    
    # If its not a creature it won't have power or toughness value to write
    line4 = ''
    if 'power' in card:
        line4 = f'\n{card["power"]} / {card["toughness"]}'
    cardstring = line1 + line2 + line3 + line4
    
    # If it is a backside of a card, Each line is indented 
    if back:
        cardstring = textwrap.indent(cardstring, '     ')
    return cardstring

def write_card(card):
    # Checks if the card has two sides to write both
    if 'card_faces' in card:
        front = write_cardside(card['card_faces'][0])
        back = write_cardside(card['card_faces'][1], back=True)
        cardstring = front + os.linesep + back
        
    # Otherwise just writes the front side
    else:
        cardstring = write_cardside(card)
    
    return cardstring

with open("standard_cards.txt", 'w', encoding='utf-8') as f:
    for card in cards:
        f.write(write_card(card))
        f.write(os.linesep)